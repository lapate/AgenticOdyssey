# Environment Setup Guide

This guide walks you through setting up everything you need for the AgenticOdyssey workshop.

## 1. System Requirements

| Tool | Minimum Version | Install Link |
|------|----------------|--------------|
| Python | 3.10+ | https://www.python.org/downloads/ |
| Git | 2.40+ | https://git-scm.com/downloads |
| VS Code | Latest | https://code.visualstudio.com/ |
| Azure CLI | 2.60+ | https://docs.microsoft.com/cli/azure/install-azure-cli |
| Docker Desktop | 4.x | https://www.docker.com/products/docker-desktop/ |

---

## 2. Azure Setup

### 2.1 Create an Azure OpenAI Resource

1. Sign in to the [Azure Portal](https://portal.azure.com)
2. Search for **Azure OpenAI** and click **Create**
3. Fill in the required fields:
   - **Subscription:** Your subscription
   - **Resource Group:** Create new → `rg-agentic-odyssey`
   - **Region:** `East US 2` or `Sweden Central` (recommended for latest models)
   - **Name:** `aoai-agentic-odyssey-<unique-suffix>`
   - **Pricing Tier:** `Standard S0`
4. Click **Review + Create** → **Create**

### 2.2 Deploy a Model

1. Open [Azure OpenAI Studio](https://oai.azure.com)
2. Go to **Deployments** → **Create new deployment**
3. Select model: **gpt-4o** (latest version)
4. Deployment name: `gpt-4o` (used throughout the labs)
5. Click **Create**

### 2.3 Retrieve Your Credentials

1. In the Azure Portal, open your Azure OpenAI resource
2. Go to **Keys and Endpoint**
3. Copy **Key 1** and the **Endpoint**

---

## 3. Local Environment Setup

### 3.1 Clone the Repository

```bash
git clone https://github.com/lapate/AgenticOdyssey.git
cd AgenticOdyssey
```

### 3.2 Create a Python Virtual Environment

```bash
# Create the environment
python -m venv .venv

# Activate it
source .venv/bin/activate        # Linux / macOS
.venv\Scripts\activate           # Windows (Command Prompt)
.venv\Scripts\Activate.ps1       # Windows (PowerShell)
```

### 3.3 Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3.4 Configure Environment Variables

```bash
# Copy the example file
cp .env.example .env

# Open and edit .env with your Azure credentials
code .env
```

Fill in the following values in `.env`:

```dotenv
AZURE_OPENAI_ENDPOINT=https://<your-resource-name>.openai.azure.com/
AZURE_OPENAI_API_KEY=<your-key-1>
AZURE_OPENAI_API_VERSION=2024-12-01-preview
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o
```

> ⚠️ **Never commit your `.env` file** — it is listed in `.gitignore`.

---

## 4. VS Code Extensions

Install the following VS Code extensions for the best experience:

1. **GitHub Copilot** — `GitHub.copilot`
2. **GitHub Copilot Chat** — `GitHub.copilot-chat`
3. **Python** — `ms-python.python`
4. **Pylance** — `ms-python.vscode-pylance`
5. **Azure Tools** — `ms-vscode.vscode-node-azure-pack`

Install via the command line:

```bash
code --install-extension GitHub.copilot
code --install-extension GitHub.copilot-chat
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
```

---

## 5. Verify Your Setup

Run the validation script to confirm everything is configured correctly:

```bash
python docs/validate_setup.py
```

Expected output:

```
✅ Python 3.10+         OK
✅ openai package       OK
✅ azure-identity       OK
✅ pyautogen            OK
✅ .env file found      OK
✅ Azure OpenAI ping    OK  (model: gpt-4o)
```

---

## 6. Troubleshooting

### `ModuleNotFoundError` after installing requirements

Make sure your virtual environment is **activated** before running `pip install`:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

### Azure OpenAI returns 401 Unauthorized

- Double-check that `AZURE_OPENAI_API_KEY` in your `.env` is correct.
- Ensure you copied **Key 1** (not Key 2) from the Azure Portal.
- Check that the key has not expired or been rotated.

### Azure OpenAI returns 404 Not Found

- Verify `AZURE_OPENAI_DEPLOYMENT_NAME` matches **exactly** the name you gave the deployment in Azure OpenAI Studio.
- Verify the endpoint URL ends with `/` and does not include any path segments.

### Python version is older than 3.10

Install [pyenv](https://github.com/pyenv/pyenv) to manage multiple Python versions:

```bash
pyenv install 3.11.9
pyenv local 3.11.9
```
