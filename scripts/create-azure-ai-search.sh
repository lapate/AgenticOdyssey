#!/bin/bash
set -euo pipefail

###############################################################################
# create-azure-ai-search.sh
#
# Deploys an Azure AI Search instance (Free tier), creates an index, and
# uploads the News Story markdown files from the data/ directory.
###############################################################################

# ── Variables ─────────────────────────────────────────────────────────────────
RESOURCE_GROUP="agenticodyssey-rg"
LOCATION="westus3"
SEARCH_SERVICE_NAME="${SEARCH_SERVICE_NAME:-agenticodyssey-search-$RANDOM}"
INDEX_NAME="${INDEX_NAME:-news-stories}"
API_VERSION="2024-07-01"

REPO_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"
DATA_DIR="$REPO_DIR/data"

# ── Prerequisite Checks ─────────────────────────────────────────────────────
echo "=== Checking prerequisites ==="

if ! command -v az &> /dev/null; then
    echo "ERROR: Azure CLI (az) is not installed. Run scripts/setup.sh first."
    exit 1
fi

if ! az account show &> /dev/null; then
    echo "ERROR: Not logged in to Azure. Run 'az login' first."
    exit 1
fi

if ! command -v jq &> /dev/null; then
    echo "ERROR: jq is not installed. Install it with: sudo apt install -y jq"
    exit 1
fi

if ! command -v curl &> /dev/null; then
    echo "ERROR: jq is not installed. Install it with: sudo apt install -y curl"
    exit 1
fi

echo "All prerequisites met."

# ── Create Resource Group ────────────────────────────────────────────────────
echo ""
echo "=== Creating resource group: $RESOURCE_GROUP ==="
az group create \
    --name "$RESOURCE_GROUP" \
    --location "$LOCATION" \
    --output none

echo "Resource group '$RESOURCE_GROUP' ready."

# ── Create Azure AI Search Service (Free tier) ──────────────────────────────
echo ""
echo "=== Creating Azure AI Search service: $SEARCH_SERVICE_NAME (Free tier) ==="
az search service create \
    --name "$SEARCH_SERVICE_NAME" \
    --resource-group "$RESOURCE_GROUP" \
    --sku free \
    --location "$LOCATION" \
    --output none

echo "Search service '$SEARCH_SERVICE_NAME' created."

# ── Retrieve Admin API Key ───────────────────────────────────────────────────
echo ""
echo "=== Retrieving admin API key ==="
ADMIN_KEY=$(az search admin-key show \
    --service-name "$SEARCH_SERVICE_NAME" \
    --resource-group "$RESOURCE_GROUP" \
    --query primaryKey \
    --output tsv)


SEARCH_ENDPOINT="https://${SEARCH_SERVICE_NAME}.search.windows.net"


echo "Admin key retrieved."

# ── Create Search Index ──────────────────────────────────────────────────────
echo ""
echo "=== Creating search index: $INDEX_NAME ==="

INDEX_SCHEMA=$(cat <<'EOF'
{
  "name": "INDEX_NAME_PLACEHOLDER",
  "fields": [
    { "name": "id",      "type": "Edm.String", "key": true,  "searchable": false, "filterable": false, "sortable": false, "facetable": false },
    { "name": "title",   "type": "Edm.String", "key": false, "searchable": true,  "filterable": false, "sortable": false, "facetable": false },
    { "name": "date",    "type": "Edm.String", "key": false, "searchable": false, "filterable": true,  "sortable": true,  "facetable": false },
    { "name": "type",    "type": "Edm.String", "key": false, "searchable": true,  "filterable": true,  "sortable": false, "facetable": true  },
    { "name": "region",  "type": "Edm.String", "key": false, "searchable": true,  "filterable": true,  "sortable": false, "facetable": true  },
    { "name": "content", "type": "Edm.String", "key": false, "searchable": true,  "filterable": false, "sortable": false, "facetable": false }
  ]
}
EOF
)

# Substitute the actual index name
INDEX_SCHEMA=$(echo "$INDEX_SCHEMA" | sed "s/INDEX_NAME_PLACEHOLDER/$INDEX_NAME/")

curl -s -X PUT \
    "${SEARCH_ENDPOINT}/indexes/${INDEX_NAME}?api-version=${API_VERSION}" \
    -H "Content-Type: application/json" \
    -H "api-key: ${ADMIN_KEY}" \
    -d "$INDEX_SCHEMA" \
    --output /dev/null \
    --fail-with-body

echo "Index '$INDEX_NAME' created."

# ── Upload News Story Documents ──────────────────────────────────────────────
echo ""
echo "=== Uploading News Story documents ==="

# Start building the batch payload
DOCS_JSON='{"value":['
FIRST=true

for filepath in "$DATA_DIR"/News\ Story*.md; do
    [ -f "$filepath" ] || continue

    filename=$(basename "$filepath")
    echo "  Processing: $filename"

    # Generate a stable ID from the filename (lowercase, alphanumeric + hyphens)
    doc_id=$(echo "$filename" | sed 's/\.md$//' | sed 's/[^a-zA-Z0-9]/-/g' | tr '[:upper:]' '[:lower:]' | sed 's/--*/-/g' | sed 's/^-//;s/-$//')

    # Read the full file content
    file_content=$(cat "$filepath")

    # Extract metadata using grep/sed
    title=$(echo "$file_content" | grep -m1 '^# ' | sed 's/^# //')
    date_val=$(echo "$file_content" | grep -m1 '^\*\*Date:\*\*' | sed 's/.*\*\*Date:\*\* *//')
    type_val=$(echo "$file_content" | grep -m1 '^\*\*Type:\*\*' | sed 's/.*\*\*Type:\*\* *//')
    region_val=$(echo "$file_content" | grep -m1 '^\*\*Region:\*\*' | sed 's/.*\*\*Region:\*\* *//')

    # Build a JSON document using jq for safe escaping
    doc_json=$(jq -n \
        --arg id "$doc_id" \
        --arg title "$title" \
        --arg date "$date_val" \
        --arg type "$type_val" \
        --arg region "$region_val" \
        --arg content "$file_content" \
        '{
            "@search.action": "upload",
            "id": $id,
            "title": $title,
            "date": $date,
            "type": $type,
            "region": $region,
            "content": $content
        }')

    if [ "$FIRST" = true ]; then
        FIRST=false
    else
        DOCS_JSON+=","
    fi
    DOCS_JSON+="$doc_json"
done

DOCS_JSON+=']}'

# Push the batch to the index
HTTP_CODE=$(curl -s -o /tmp/search-upload-response.json -w "%{http_code}" \
    -X POST \
    "${SEARCH_ENDPOINT}/indexes/${INDEX_NAME}/docs/index?api-version=${API_VERSION}" \
    -H "Content-Type: application/json" \
    -H "api-key: ${ADMIN_KEY}" \
    -d "$DOCS_JSON")

if [ "$HTTP_CODE" -ge 200 ] && [ "$HTTP_CODE" -lt 300 ]; then
    echo "Documents uploaded successfully (HTTP $HTTP_CODE)."
else
    echo "ERROR: Document upload failed (HTTP $HTTP_CODE)."
    cat /tmp/search-upload-response.json
    echo "ERROR: HTTP POST of the example newstories has failed. Check your variables and that the AI Search was created in the Azure portal."
fi

# ── Verify Document Count ────────────────────────────────────────────────────
echo ""
echo "=== Verifying index ==="

# Give the index a moment to process
sleep 3

DOC_COUNT=$(curl -s \
    "${SEARCH_ENDPOINT}/indexes/${INDEX_NAME}/docs/\$count?api-version=${API_VERSION}" \
    -H "api-key: ${ADMIN_KEY}")

echo "Documents in index '$INDEX_NAME': $DOC_COUNT"

# ── Print Connection Info ────────────────────────────────────────────────────
echo ""
echo "==========================================="
echo "  Azure AI Search Deployment Complete"
echo "==========================================="
echo "  Resource Group : $RESOURCE_GROUP"
echo "  Search Service : $SEARCH_SERVICE_NAME"
echo "  Endpoint       : $SEARCH_ENDPOINT"
echo "  Index Name     : $INDEX_NAME"
echo "  Admin Key      : $ADMIN_KEY"
echo "  Documents      : $DOC_COUNT"
echo "==========================================="
echo ""
echo "Test with:"
echo "  curl -s '${SEARCH_ENDPOINT}/indexes/${INDEX_NAME}/docs?api-version=${API_VERSION}&search=chicken&\$top=3' -H api-key: '${ADMIN_KEY}' | jq ."
