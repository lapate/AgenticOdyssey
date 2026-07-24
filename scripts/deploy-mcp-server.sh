#!/bin/bash
set -euo pipefail

###############################################################################
# deploy-mcp-server.sh
#
# Deploys the MCP Server container to Azure Container Apps (HTTPS ingress).
#
# ┌─────────────────────────────────────────────────────────────────────────┐
# │  INSTRUCTIONS FOR STUDENTS                                             │
# │                                                                        │
# │  1. Edit CONTAINER_NAME below to be unique to you                      │
# │     (e.g., append your initials: "mcp-server-jsmith").                 │
# │                                                                        │
# │  2. Run `az login` to authenticate with Azure.                         │
# │                                                                        │
# │  3. Run this script:                                                   │
# │       bash scripts/deploy-mcp-server.sh                                │
# │                                                                        │
# │  4. When it finishes, it will print the MCP SSE endpoint URL.          │
# │     Use that URL to connect from Foundry or any MCP client.            │
# │                                                                        │
# │  5. To clean up when done:                                             │
# │       az group delete --name agenticodyssey-rg --yes --no-wait         │
# └─────────────────────────────────────────────────────────────────────────┘
###############################################################################

# ── STUDENT: Edit these variables ────────────────────────────────────────────
# CONTAINER_NAME : Name for the container app (must be unique to you).
#                  Example: "mcp-server-jsmith"
CONTAINER_NAME="${CONTAINER_NAME:-mcp-server}"

# IMAGE_TAG : The container image tag to deploy. Use "latest" for the most
#             recent build, or a specific run tag like "run-5".
IMAGE_TAG="${IMAGE_TAG:-latest}"
# ─────────────────────────────────────────────────────────────────────────────

# ── Fixed values (do not change) ─────────────────────────────────────────────
RESOURCE_GROUP="agenticodyssey-rg"
LOCATION="westus3"
ENVIRONMENT="agenticodyssey-mcp-env"
# ─────────────────────────────────────────────────────────────────────────────

# ── Derived values (no need to edit) ─────────────────────────────────────────
IMAGE="ghcr.io/lapate/agenticodyssey/mcp-server:${IMAGE_TAG}"
PORT=8000

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

SUBSCRIPTION=$(az account show --query name --output tsv)
echo "Logged in. Subscription: $SUBSCRIPTION"
echo "Image: $IMAGE"
echo ""

# ── Create Resource Group ────────────────────────────────────────────────────
echo "=== Creating resource group: $RESOURCE_GROUP ==="
az group create \
    --name "$RESOURCE_GROUP" \
    --location "$LOCATION" \
    --output none

echo "Resource group '$RESOURCE_GROUP' ready."
echo ""

# ── Ensure Container Apps prerequisites ──────────────────────────────────────
echo "=== Ensuring Azure Container Apps extension and providers ==="
az extension add --name containerapp --upgrade --only-show-errors
az provider register --namespace Microsoft.App --wait
az provider register --namespace Microsoft.OperationalInsights --wait
echo "Extension and providers ready."
echo ""

# ── Create Container Apps Environment ────────────────────────────────────────
echo "=== Ensuring Container Apps environment: $ENVIRONMENT ==="
if az containerapp env show --name "$ENVIRONMENT" --resource-group "$RESOURCE_GROUP" &> /dev/null; then
    echo "Environment '$ENVIRONMENT' already exists — reusing it."
else
    echo "Creating environment '$ENVIRONMENT' (this can take 3-5 minutes)..."
    az containerapp env create \
        --name "$ENVIRONMENT" \
        --resource-group "$RESOURCE_GROUP" \
        --location "$LOCATION" \
        --output none
fi
echo ""

# ── Deploy Container App ─────────────────────────────────────────────────────
echo "=== Deploying container app: $CONTAINER_NAME ==="
if az containerapp show --name "$CONTAINER_NAME" --resource-group "$RESOURCE_GROUP" &> /dev/null; then
    echo "Container app exists — updating to image $IMAGE..."
    az containerapp update \
        --name "$CONTAINER_NAME" \
        --resource-group "$RESOURCE_GROUP" \
        --image "$IMAGE" \
        --output none
else
    az containerapp create \
        --name "$CONTAINER_NAME" \
        --resource-group "$RESOURCE_GROUP" \
        --environment "$ENVIRONMENT" \
        --image "$IMAGE" \
        --target-port "$PORT" \
        --ingress external \
        --transport auto \
        --cpu 1 --memory 2Gi \
        --min-replicas 1 --max-replicas 1 \
        --output none
fi

echo "Container app '$CONTAINER_NAME' deployed."
echo ""

# ── Get HTTPS Endpoint (FQDN) ────────────────────────────────────────────────
echo "=== Retrieving HTTPS endpoint ==="
FQDN=$(az containerapp show \
    --name "$CONTAINER_NAME" \
    --resource-group "$RESOURCE_GROUP" \
    --query "properties.configuration.ingress.fqdn" \
    --output tsv)

# ── Print Connection Info ────────────────────────────────────────────────────
echo ""
echo "==========================================="
echo "  MCP Server Deployment Complete"
echo "==========================================="
echo "  Resource Group : $RESOURCE_GROUP"
echo "  Environment    : $ENVIRONMENT"
echo "  Container App  : $CONTAINER_NAME"
echo "  Location       : $LOCATION"
echo "  Image          : $IMAGE"
echo "  Public FQDN    : $FQDN"
echo ""
echo "  MCP SSE Endpoint:"
echo "    https://${FQDN}/sse"
echo ""
echo "==========================================="
echo ""
echo "Use this endpoint URL in Foundry or any MCP client."
echo ""
echo "NOTE: Azure Container Apps serves this over HTTPS on port 443, which"
echo "      Foundry's MCP tool requires. If a fresh deployment briefly reports"
echo "      'blocked by outbound SSRF protection', the revision is still"
echo "      starting -- wait a minute and reconnect."
echo ""
echo "To clean up resources when done:"
echo "  az group delete --name $RESOURCE_GROUP --yes --no-wait"
