# Agentic Odyssey — Participant Guide

Welcome to **Agentic Odyssey**! In this lab you will deploy a live MCP (Model Context Protocol) server and an Azure AI Search index, then connect them to Microsoft Foundry to build an AI agent that can query real chicken-store sales data.

By the end of setup you will have:
- ✅ A running **MCP Server** hosted in Azure (Container Instance) exposing 10 CRUD tools over SSE
- ✅ An **Azure AI Search** index populated with news-story documents
- ✅ Both endpoints ready to wire into a Foundry agent

---

## Table of Contents

1. [Open the Lab in GitHub Codespaces](#1-open-the-lab-in-github-codespaces)
2. [Wait for Automatic Setup](#2-wait-for-automatic-setup)
3. [Log In to Azure](#3-log-in-to-azure)
4. [Deploy the MCP Server](#4-deploy-the-mcp-server)
5. [Deploy Azure AI Search](#5-deploy-azure-ai-search)
6. [Record Your Endpoints](#6-record-your-endpoints)
7. [Cleaning Up](#7-cleaning-up)

---

## 1. Open the Lab in GitHub Codespaces

1. Navigate to this repository on GitHub: **https://github.com/lapate/AgenticOdyssey**
2. Click the green **`<> Code`** button → select the **Codespaces** tab
3. Click **"Create codespace on main"**

> 📸 **HUMAN — DO THIS:** Take a screenshot of the GitHub repository page with the **Code → Codespaces** dropdown open, showing the "Create codespace on main" button.

The codespace will open in a browser-based VS Code window. The very first time it loads it will automatically run the environment setup script — you will see terminal activity at the bottom of the screen.

---

## 2. Wait for Automatic Setup

The devcontainer is configured to automatically run `scripts/setup.sh` after the environment is created. This script:

- Installs **Azure CLI** (if not already present)
- Installs **uv** (fast Python package manager)
- Creates a Python virtual environment
- Installs all Python dependencies from `requirements.txt`

**Wait for the terminal to finish and show no errors before proceeding.**

> 📸 **HUMAN — DO THIS:** Take a screenshot of the VS Code terminal after `scripts/setup.sh` completes successfully (green output / no errors visible).

---

## 3. Log In to Azure

Open a new terminal in the codespace (**Terminal → New Terminal**) and run:

```bash
az login --use-device-code
```

> **Why `--use-device-code`?** Codespaces run in a remote container and can't open a browser directly. This command gives you a short code to enter at [https://microsoft.com/devicelogin](https://microsoft.com/devicelogin) from your local browser.

You will see output like:

```
To sign in, use a web browser to open the page https://microsoft.com/devicelogin
and enter the code XXXXXXXX to authenticate.
```

1. Copy the code from the terminal
2. Open **https://microsoft.com/devicelogin** in your browser
3. Enter the code and sign in with your Azure credentials
4. Return to the codespace — you should see your subscription listed

> 📸 **HUMAN — DO THIS:** Take a screenshot of the device login page at **microsoft.com/devicelogin** showing the code-entry box (before entering the code). Also take a screenshot of the codespace terminal after successful login showing the subscription list.

Confirm the correct subscription is active:

```bash
az account show --output table
```

If you need to switch subscriptions:

```bash
az account set --subscription "<Your Subscription Name or ID>"
```

---

## 4. Deploy the MCP Server

The MCP server is a containerized FastMCP application that exposes CRUD tools for chicken-store data over HTTP (SSE protocol). It is already built and published to GitHub Packages — you just need to deploy it to Azure.

### 4a. Edit the deployment variables

Open `scripts/deploy-mcp-server.sh` in the editor. Find the **"STUDENT: Edit these variables"** section near the top and update the two required values to be unique to you:

```bash
# ── STUDENT: Edit these variables ────────────────────────────────────────
RESOURCE_GROUP="${RESOURCE_GROUP:-mcp-lab-rg}"       # ← Change this
CONTAINER_NAME="${CONTAINER_NAME:-mcp-server}"        # ← Change this
```

**Rules:**
- Use only lowercase letters, numbers, and hyphens
- Append your initials or a short unique string so you don't collide with other students
- Example: `mcp-lab-jsmith-rg` and `mcp-server-jsmith`

Leave `LOCATION` as `westus3` and `IMAGE_TAG` as `latest`.

> 📸 **HUMAN — DO THIS:** Take a screenshot of `scripts/deploy-mcp-server.sh` open in the VS Code editor with the two variables highlighted/edited.

### 4b. Run the script

```bash
bash scripts/deploy-mcp-server.sh
```

The script will:
1. Verify your Azure login
2. Create a resource group in `westus3`
3. Pull the pre-built container image from `ghcr.io/lapate/agenticodyssey/mcp-server:latest`
4. Launch an Azure Container Instance with a public IP on port 8000
5. Print your endpoint URL

Deployment takes approximately **1–2 minutes**.

### 4c. Save your MCP endpoint

When the script finishes you will see output like:

```
===========================================
  MCP Server Deployment Complete
===========================================
  Resource Group : mcp-lab-jsmith-rg
  Container      : mcp-server-jsmith
  Location       : westus3
  Image          : ghcr.io/lapate/agenticodyssey/mcp-server:latest
  Public IP      : 20.x.x.x

  MCP SSE Endpoint:
    http://20.x.x.x:8000/sse

===========================================
```

📌 **Copy and save the SSE endpoint URL** — you will need it when configuring your Foundry agent.

> 📸 **HUMAN — DO THIS:** Take a screenshot of the terminal showing the successful deployment output with the MCP SSE Endpoint URL visible.

---

## 5. Deploy Azure AI Search

Next, deploy an Azure AI Search instance and populate it with the lab's news-story documents.

### 5a. (Optional) Review the variables

Open `scripts/create-azure-ai-search.sh`. The defaults work fine for most students, but if you want a custom resource group name, you can update:

```bash
RESOURCE_GROUP="${RESOURCE_GROUP:-agenticodyssey-rg}"         # ← Optionally change
SEARCH_SERVICE_NAME="${SEARCH_SERVICE_NAME:-agenticodyssey-search-$RANDOM}"  # auto-unique
```

Leave `LOCATION` as `westus3`.

> 📸 **HUMAN — DO THIS:** Take a screenshot of `scripts/create-azure-ai-search.sh` open in the editor showing the variables section.

### 5b. Install jq (required by the script)

```bash
sudo apt install -y jq
```

### 5c. Run the script

```bash
bash "scripts/create -azure-ai-search.sh"
```

> ⚠️ Note the quotes around the script path — the filename contains a space.

The script will:
1. Create a resource group (reuses the existing one if it already exists)
2. Provision an Azure AI Search service (Free tier) in `westus3`
3. Create a `news-stories` index with title, date, type, region, and content fields
4. Upload all news-story documents from the `data/` directory
5. Print the search endpoint URL and admin key

This takes approximately **3–5 minutes** while the search service provisions.

### 5d. Save your Search endpoint and key

When complete you will see:

```
===========================================
  Azure AI Search Deployment Complete
===========================================
  Resource Group : agenticodyssey-rg
  Search Service : agenticodyssey-search-12345
  Endpoint       : https://agenticodyssey-search-12345.search.windows.net
  Index Name     : news-stories
  Admin Key      : xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  Documents      : 10
===========================================
```

📌 **Copy and save both the Endpoint URL and the Admin Key** — you will need these in the Foundry configuration.

> 📸 **HUMAN — DO THIS:** Take a screenshot of the terminal showing the successful Azure AI Search deployment output with the Endpoint and Admin Key visible.

---

## 6. Record Your Endpoints

Before moving on to the lab exercises, make sure you have noted down all three values:

| Value | Where to find it |
|-------|-----------------|
| **MCP SSE Endpoint** | Output of `deploy-mcp-server.sh` — looks like `http://<IP>:8000/sse` |
| **Search Endpoint** | Output of `create-azure-ai-search.sh` — looks like `https://<name>.search.windows.net` |
| **Search Admin Key** | Output of `create-azure-ai-search.sh` — 32-character alphanumeric string |

You are now ready for the lab exercises. Your instructor will guide you through connecting these endpoints to Microsoft Foundry.

---

## 7. Cleaning Up

When the lab is complete, delete your Azure resources to avoid charges:

```bash
# Delete the MCP server resource group (replace with your actual name)
az group delete --name mcp-lab-<your-initials>-rg --yes --no-wait

# Delete the AI Search resource group
az group delete --name agenticodyssey-rg --yes --no-wait
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `az: command not found` | Run `bash scripts/setup.sh` to reinstall the Azure CLI |
| `Not logged in to Azure` | Run `az login --use-device-code` again |
| `az account show` shows wrong subscription | Run `az account set --subscription "<name>"` |
| MCP script fails with image pull error | Verify image tag: `ghcr.io/lapate/agenticodyssey/mcp-server:latest` is public |
| Search script fails with `jq not found` | Run `sudo apt install -y jq` first |
| Container IP shows as empty | Wait 30 seconds and re-run: `az container show --resource-group <rg> --name <name> --query ipAddress.ip -o tsv` |
