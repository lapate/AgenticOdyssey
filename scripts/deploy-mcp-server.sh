#!/bin/bash
set -euo pipefail

###############################################################################
# deploy-mcp-server.sh
#
# Deploys the MCP Server container to Azure Container Instances (ACI).
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
# CONTAINER_NAME : Name for the container instance (must be unique to you).
#                  Example: "mcp-server-jsmith"
CONTAINER_NAME="${CONTAINER_NAME:-mcp-server}"

# IMAGE_TAG : The container image tag to deploy. Use "latest" for the most
#             recent build, or a specific run tag like "run-5".
IMAGE_TAG="${IMAGE_TAG:-latest}"
# ─────────────────────────────────────────────────────────────────────────────

# ── Fixed values (do not change) ─────────────────────────────────────────────
RESOURCE_GROUP="agenticodyssey-rg"
LOCATION="westus3"
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

# ── Deploy Container Instance ────────────────────────────────────────────────
echo "=== Deploying container: $CONTAINER_NAME ==="
az container create \
    --resource-group "$RESOURCE_GROUP" \
    --name "$CONTAINER_NAME" \
    --image "$IMAGE" \
    --ports "$PORT" \
    --ip-address Public \
    --location "$LOCATION" \
    --cpu 1 \
    --memory 1 \
    --os-type Linux \
    --restart-policy Always \
    --output none

echo "Container '$CONTAINER_NAME' deployed."
echo ""

# ── Get Public IP ────────────────────────────────────────────────────────────
echo "=== Retrieving public IP ==="
IP_ADDRESS=$(az container show \
    --resource-group "$RESOURCE_GROUP" \
    --name "$CONTAINER_NAME" \
    --query ipAddress.ip \
    --output tsv)

# ── Print Connection Info ────────────────────────────────────────────────────
echo ""
echo "==========================================="
echo "  MCP Server Deployment Complete"
echo "==========================================="
echo "  Resource Group : $RESOURCE_GROUP"
echo "  Container      : $CONTAINER_NAME"
echo "  Location       : $LOCATION"
echo "  Image          : $IMAGE"
echo "  Public IP      : $IP_ADDRESS"
echo ""
echo "  MCP SSE Endpoint:"
echo "    http://${IP_ADDRESS}:${PORT}/sse"
echo ""
echo "==========================================="
echo ""
echo "Use this endpoint URL in Foundry or any MCP client."
echo ""
echo "To clean up resources when done:"
echo "  az group delete --name $RESOURCE_GROUP --yes --no-wait"
