# Lab: Create the Inventory Agent

In this lab you will build a **Chicken Store Inventory Agent** in Microsoft Foundry. The agent connects to the live MCP server you deployed in the setup steps and can read, update, and answer questions about chicken store sales and financial data in real time.

By the end of this lab you will have:
- ✅ A named Foundry agent with a custom system prompt
- ✅ The MCP server connected as a live tool
- ✅ A working agent you can query about store inventory and financials

---

## What You'll Need

Before starting, make sure you have:

| Item | Where to get it |
|------|----------------|
| **MCP SSE Endpoint URL** | Output of `scripts/deploy-mcp-server.sh` — looks like `http://<IP>:8000/sse` |
| **Azure AI Foundry project** | Your instructor will provide the project URL or you will create one |

> ⚠️ **Your MCP endpoint IP address is unique to your deployment.** It was printed at the end of the `deploy-mcp-server.sh` output. If you lost it, run this to retrieve it:
> ```bash
> az container show --resource-group agenticodyssey-rg --name ckriutz-mcp-server \
>   --query ipAddress.ip --output tsv
> ```
> Then add `:8000/sse` to form your full endpoint.

---

## Step 1: Open Microsoft Foundry

1. Go to **[https://ai.azure.com](https://ai.azure.com)** and sign in with your Azure credentials.
2. In the left navigation, select your **Hub** and then your **Project**.

> 📸 **HUMAN — DO THIS:** Take a screenshot of the Azure AI Foundry home page showing your project selected in the left nav.

---

## Step 2: Navigate to the Agents Playground

1. In the left sidebar, under **Build**, click **Agents**.
2. You will see the Agents playground with any existing agents listed.

> 📸 **HUMAN — DO THIS:** Take a screenshot of the Agents section showing the empty or existing agents list.

---

## Step 3: Create a New Agent

1. Click **+ New agent** (or **+ Create**).
2. A new agent configuration panel will open on the right.

> 📸 **HUMAN — DO THIS:** Take a screenshot of the new agent panel just after clicking "+ New agent", before filling anything in.

---

## Step 4: Name the Agent and Select a Model

1. In the **Name** field, enter:
   ```
   ChickenStoreInventoryAgent
   ```

2. Under **Model**, select **`gpt-4o`** (or the model your instructor specifies).

3. Leave the **Deployment** set to the default deployment for that model.

> 📸 **HUMAN — DO THIS:** Take a screenshot showing the agent name and model selection filled in.

---

## Step 5: Write the System Prompt

The system prompt tells the agent who it is and what it can do. In the **Instructions** box, paste the following:

```
You are ChickenStoreInventoryAgent, an AI assistant for Cluck & Co. chicken stores.

You have access to live store data through a set of tools. You can:
- Look up daily financial records (chickens bought, sold, revenue, profit) by date and store
- Look up hourly sales data (chickens cooked and sold by hour) by date, store, and hour
- Create new records when inventory is received or sales are logged
- Update existing records to correct errors or reflect adjustments
- Delete records that were entered in error

When answering questions:
- Always use the tools to retrieve live data — never make up numbers
- When asked about a specific store or date, filter your queries accordingly
- Present financial figures clearly, using USD formatting where appropriate
- If asked to make a change, confirm the record ID and the new values before updating
- Be concise but complete in your responses

Available stores: Store-001
Available dates in system: 2026-02-20 through 2026-02-28 (use list tools to discover exact records)
```

> 📸 **HUMAN — DO THIS:** Take a screenshot of the Instructions box with the full system prompt entered.

---

## Step 6: Add the MCP Server as a Tool

This is the key step — connecting your live MCP server so the agent has access to the real data tools.

1. In the agent configuration panel, scroll down to the **Tools** section (or **Actions**, depending on your Foundry version).
2. Click **+ Add tool** (or **+ Add action**).
3. Select **MCP Server** from the tool type list.

> 📸 **HUMAN — DO THIS:** Take a screenshot of the "Add tool" dropdown with MCP Server visible as an option.

4. In the **Server URL** field, enter your MCP SSE endpoint:
   ```
   http://<YOUR-IP>:8000/sse
   ```
   Replace `<YOUR-IP>` with the IP address from your `deploy-mcp-server.sh` output.

   > **Example:** `http://4.227.57.55:8000/sse`

5. Foundry will connect to the server and **automatically discover all available tools**. You should see all 10 tools appear:

   | Tool | Description |
   |------|-------------|
   | `list_daily_financials` | List daily order/financial records (filterable by date, store) |
   | `get_daily_financial` | Get one record by ID |
   | `create_daily_financial` | Add a new daily record |
   | `update_daily_financial` | Modify an existing daily record |
   | `delete_daily_financial` | Remove a daily record |
   | `list_hourly_sales` | List hourly sales (filterable by date, store, hour) |
   | `get_hourly_sale` | Get one hourly record by ID |
   | `create_hourly_sale` | Add a new hourly record |
   | `update_hourly_sale` | Modify an existing hourly record |
   | `delete_hourly_sale` | Remove an hourly record |

6. Click **Save** or **Confirm** to add the MCP server.

> 📸 **HUMAN — DO THIS:** Take a screenshot showing the 10 MCP tools successfully loaded in the Tools section.

---

## Step 7: Save the Agent

1. Click **Save** (or **Apply**) to save your agent configuration.
2. Note the **Agent ID** shown in the panel — you will need this in later labs.

> 📸 **HUMAN — DO THIS:** Take a screenshot of the saved agent configuration showing the Agent ID.

---

## Step 8: Test the Agent

With the agent saved, test it in the chat panel on the right side of the playground.

### Test 1 — List all daily records
```
Show me all the daily financial records you have access to.
```
**Expected:** The agent calls `list_daily_financials`, returns 10 records with dates, store IDs, and financial figures.

> 📸 **HUMAN — DO THIS:** Take a screenshot of the agent's response to this query, including the tool call visible in the trace.

---

### Test 2 — Query by date
```
What were the financials for Store-001 on February 22nd, 2026?
```
**Expected:** The agent calls `list_daily_financials` with `date="2026-02-22"` and `store_id="Store-001"` and returns the record.

---

### Test 3 — Hourly sales
```
How many chickens were sold hour by hour at Store-001 on February 20th?
```
**Expected:** The agent calls `list_hourly_sales` with date and store filters, returns 13 hourly records.

> 📸 **HUMAN — DO THIS:** Take a screenshot of the agent responding to the hourly sales query showing the breakdown by hour.

---

### Test 4 — Update a record
```
The chickens sold total for Store-001 on February 21st should be 115, not 111. Please correct that.
```
**Expected:** The agent:
1. Calls `list_daily_financials` to find the record
2. Confirms the record ID and current value with you
3. Calls `update_daily_financial` with the corrected value
4. Returns the updated record

> 📸 **HUMAN — DO THIS:** Take a screenshot of the full update interaction showing the before/after values.

---

### Test 5 — Reasoning question
```
Which day had the highest gross profit? How does that compare to the lowest?
```
**Expected:** The agent retrieves all records and reasons over them to identify the best and worst performing days.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| MCP server URL not accepted | Ensure the URL is `http://` not `https://`, and includes the full path: `http://<IP>:8000/sse` |
| Tools not discovered | Verify the container is still running: `az container show --resource-group agenticodyssey-rg --name ckriutz-mcp-server --query instanceView.state -o tsv` |
| Agent returns "I don't have access to data" | Check that the MCP tool is enabled (toggle is on) in the Tools section |
| Container IP changed | Re-run `scripts/deploy-mcp-server.sh` — it prints the current IP at the end |

---

## What You Built

- A **ChickenStoreInventoryAgent** that connects to a live containerized MCP server
- The agent can read, create, update, and delete real inventory records
- It reasons over live data — no hardcoded information in the prompt

In the next lab, you will orchestrate this agent from Python code and combine it with additional data sources.
