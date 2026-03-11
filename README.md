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

### Labs

- **[Lab 1 — Create the Inventory Agent](labs/create-inventory-agent.md)**
- **[Lab 2 — Create the Sales Insights Agent](labs/create-insights-agent.md)**

---

## 1. Open the Lab in GitHub Codespaces

1. Navigate to this repository on GitHub: **https://github.com/lapate/AgenticOdyssey**
2. Click the green **`<> Code`** button → select the **Codespaces** tab
3. Click **"Create codespace on main"**

![alt text](/docs/create_codespace_on_main.png)

The codespace will open in a browser-based VS Code window. The environment will automatically set itself up — you will see terminal activity at the bottom of the screen as it installs dependencies.

---

## 2. Wait for Automatic Setup

The devcontainer is configured to automatically install everything you need:

- **Azure CLI** — installed via a devcontainer feature (no script required)
- **git-lfs** — installed via a devcontainer feature
- **Python dependencies** — installed from `requirements.txt` automatically

This happens in the background when the codespace first starts. **Wait for the terminal activity to finish before proceeding.**

> ℹ️ `scripts/setup.sh` exists in the repo but is **not** used by the devcontainer — it is only needed if you are setting up a local environment outside of Codespaces.

---

## 3. Log In to Azure

Open a new terminal in the codespace (**Terminal → New Terminal**) and run:

```bash
az login --use-device-code
```

🤔 NOTE: Login using your personal Azure account, not your corp @microsoft.com account.

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

![alt text](/docs/device-code.png)

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

Open `scripts/deploy-mcp-server.sh` in the editor. Find the **"STUDENT: Edit these variables"** section near the top and update `CONTAINER_NAME` to be unique to you:

```bash
# ── STUDENT: Edit these variables ────────────────────────────────────────
CONTAINER_NAME="${CONTAINER_NAME:-mcp-server}"   # ← Change this
```

**Rules:**
- Use only lowercase letters, numbers, and hyphens
- Append your initials or a short unique string
- Example: `mcp-server-jsmith`

> **Note:** `RESOURCE_GROUP` (`agenticodyssey-rg`) and `LOCATION` (`westus3`) are already set for the lab — do not change them.

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

![alt text](/docs/mcp_success.png)

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

### 5b. Run the script

```bash
bash scripts/create-azure-ai-search.sh
```

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

![alt text](/docs/ai-search-success.png)

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
# Delete all lab resources (both MCP server and AI Search share this group)
az group delete --name agenticodyssey-rg --yes --no-wait
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `az: command not found` | Run `bash scripts/setup.sh` to reinstall the Azure CLI |
| `Not logged in to Azure` | Run `az login --use-device-code` again |
| `az account show` shows wrong subscription | Run `az account set --subscription "<name>"` |
| `AuthorizationFailed` — does not have authorization to perform action over scope | You're logged into the wrong subscription. Run `az account list` to see all available subscriptions, then run `az account set --subscription "The Name of your Subscription"` to switch to the correct one. |
| MCP script fails with image pull error | Verify image tag: `ghcr.io/lapate/agenticodyssey/mcp-server:latest` is public |
| Container IP shows as empty | Wait 30 seconds and re-run: `az container show --resource-group <rg> --name <name> --query ipAddress.ip -o tsv` |