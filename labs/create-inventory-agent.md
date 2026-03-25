# Lab: Create the Inventory Agent

In this lab you will build a **Zava Groceries Inventory Agent** in Microsoft Foundry. The agent connects to the live MCP server you deployed in the setup steps and can read, update, and answer questions about Zava Groceries sales and financial data in real time.

By the end of this lab you will have:
- ✅ A named Foundry agent with a custom system prompt.
- ✅ The MCP server connected as a live tool.
- ✅ A working agent you can query about store inventory and financials.

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
2. In the sidebar navigation pane, select your **Hub** and then your **Project**.

![alt text](/docs/azure_project.png)

---

## Step 2: Navigate to the Agents Playground

1. In the sidebar pane, under **Build**, click **Agents**. Make sure the Build tab is also selected on the top menu if you don't see the build option.
2. You will see the Agents playground with any existing agents listed.

![alt text](/docs/new_agent.png)

---

## Step 3: Create a New Agent

1. Select **+ New agent** (or **+ Create**).
2. A new agent configuration panel will open on the right.

![alt text](/docs/new_agent_name.png)

---

## Step 4: Name the Agent and Select a Model

1. In the **Name** field, enter:
   ```
   ZavaGroceriesInventoryAgent
   ```

2. Under **Model**, select **`gpt-5-mini`** (or the model your instructor specifies).

3. Leave the **Deployment** set to the default deployment for that model.

![alt text](/docs/new_agent_filled_in.png)

---

## Step 5: Write the System Prompt

The system prompt tells the agent who it is and what it can do. In the **Instructions** box, paste the following:

```
You are ZavaGroceriesInventoryAgent, an AI assistant for Zava Groceries.

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
```

![alt text](/docs/instructions.png)

---

## Step 6: Add the MCP Server as a Tool

This is the key step — connecting your live MCP server so the agent has access to the real data tools.

1. In the agent configuration panel, scroll down to the **Tools** section (or **Actions**, depending on your Foundry version).
2. Select **+ Add tool** (or **+ Add action**) and then select **Browse all tools**.
3. In the **Select a tool** dialog box, select the **Custom** pane. Select **Model Context Protocol (MCP)** and then select **Create**.

![alt text](/docs/MCP-custom-tool-create.png)

4. In the **Add Model Context Protocol tool** dialog box, give the MCP server a name and enter the MCP SSE Endpoint URL. (See the beginning of this lab for instructions, if you don't have the endpoint.)
5. In the **Authentication** field, select **`Unauthenticated`**, and then select **Connect**.

![alt text](/docs/MCP-set-authentication.png)

6. Foundry will connect to the server and **automatically discover all available tools**. You should see all 10 tools appear:

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

7. Click **Save** or **Confirm** to add the MCP server.

![alt text](/docs/mcp_tools_new.png)

---

## Step 7: Save the Agent

1. Select **Save** (or **Apply**) to save your agent configuration.
2. Note the **Agent ID** shown in the panel — you will need this in later labs.

![alt text](/docs/agent_id.png)

---

## Step 8: Test the Agent

With the agent saved, test it in the chat panel on the right side of the playground.

### Test 1 — List all the tools
```
Can you list the tools you have access to?
```
**Expected:** The agent calls `list_daily_financials`, returns 10 records with dates, store IDs, and financial figures.

![alt text](/docs/list_of_tools.png)

---

### Test 2 — Query by date
```
What were the financials for Store-001 on February 22nd, 2026?
```
**Expected:** The agent calls `list_daily_financials` with `date="2026-02-22"` and `store_id="Store-001"` and returns the record.

🤔 NOTE: You may need to approve the tool.

![alt text](/docs/approve_tool.png)

---

### Test 3 — Hourly sales
```
How many chickens were sold hour by hour at Store-001 on February 20th?
```
**Expected:** The agent calls `list_hourly_sales` with date and store filters, returns 13 hourly records.

---

### Test 4 — Update a record
```
The chickens sold total for Store-001 on February 21st should be 115, not 111. Please correct that.
```
**Expected:** The agent:
1. Calls `list_daily_financials` to find the record.
2. Confirms the record ID and current value with you.
3. Calls `update_daily_financial` with the corrected value.
4. Returns the updated record.

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
| MCP server URL not accepted | Ensure the URL is `http://` not `https://`, and includes the full path: `http://<IP>:8000/sse`. |
| Tools not discovered | Verify the container is still running: `az container show --resource-group agenticodyssey-rg --name ckriutz-mcp-server --query instanceView.state -o tsv`. |
| Agent returns "I don't have access to data" | Check that the MCP tool is enabled (toggle is on) in the Tools section. |
| Container IP changed | Re-run `scripts/deploy-mcp-server.sh` — it prints the current IP at the end. |

---

## What You Built

- A **ZavaGroceriesInventoryAgent** that connects to a live containerized MCP server.
- The agent can read, create, update, and delete real inventory records.
- It reasons over live data — no hardcoded information in the prompt.

In the next lab, you will orchestrate this agent from Python code and combine it with additional data sources.
