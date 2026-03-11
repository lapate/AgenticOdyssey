# Lab: Create the Sales Insights Agent

In this lab you will build a **Sales Insights Agent** in Microsoft Foundry. This agent combines three data sources — live store data from the MCP server, contextual news stories from Azure AI Search, and the reasoning power of the model — to identify ordering inefficiencies, recommend optimal cooking windows, and produce structured operational instructions ready to hand off to the Inventory Agent.

By the end of this lab you will have:
- ✅ A named Foundry agent with a grounded, reasoning-focused system prompt
- ✅ Azure AI Search connected as a knowledge tool (news stories)
- ✅ The MCP server connected as a live data tool
- ✅ An agent that returns actionable markdown instructions suitable for human review **or** automated handoff to another agent

---

## What You'll Need

Before starting, make sure you have completed:

| Item | Where to get it |
|------|----------------|
| **MCP SSE Endpoint URL** | Output of `scripts/deploy-mcp-server.sh` — `http://<IP>:8000/sse` |
| **Azure AI Search Endpoint** | Output of `scripts/create-azure-ai-search.sh` — `https://<name>.search.windows.net` |
| **Azure AI Search Admin Key** | Output of `scripts/create-azure-ai-search.sh` — 32-character key |
| **Azure AI Foundry project** | Your instructor will provide the project URL |
| **Lab 1 complete** | The `ZavaGroceriesInventoryAgent` from Lab 1 is built and working |

> ⚠️ **If you lost your MCP endpoint IP or Search key**, retrieve them:
> ```bash
> # MCP server IP
> az container show --resource-group agenticodyssey-rg --name {name}-mcp-server \
>   --query ipAddress.ip --output tsv
>
> # AI Search key
> az search admin-key show --service-name <your-search-service> \
>   --resource-group agenticodyssey-rg --query primaryKey --output tsv
> ```

---

## Background: What This Agent Does

The `SalesInsightsAgent` plays a different role than the Inventory Agent. Rather than executing CRUD operations, it **reasons** across multiple data sources to surface insights and produce recommendations.

It works in three layers:

```
┌─────────────────────────────────────────┐
│  Azure AI Search                        │  ← "What's happening in the world?"
│  News stories: supply chain events,     │
│  weather, local demand spikes           │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│  MCP Server (live store data)           │  ← "What are the actual numbers?"
│  Daily financials: orders, costs,       │
│  revenue, profit                        │
│  Hourly sales: cook vs. sell by hour    │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│  Model reasoning (gpt-4o)               │  ← "What should we change?"
│  Identifies waste, timing inefficiency, │
│  and context-aware ordering adjustments │
└─────────────────────────────────────────┘
```

The output is **structured markdown** — readable by a human manager, and parseable by the `ZavaGroceriesInventoryAgent` if you want to automate the changes.

---

## Step 1: Open Microsoft Foundry

1. Go to **[https://ai.azure.com](https://ai.azure.com)** and sign in.
2. Select your **Hub** and **Project** from the left nav.

![alt text](/docs/new_agent.png)

---

## Step 2: Navigate to the Agents Playground

1. In the left sidebar, under **Build**, click **Agents**.
2. You should see your `ZavaGroceriesInventoryAgent` from Lab 1 listed.

![alt text](/docs/existing_agent.png)

---

## Step 3: Create a New Agent

1. Click **+ New agent**.
2. A new agent configuration panel opens.

---

## Step 4: Name the Agent and Select a Model

1. In the **Name** field, enter:
   ```
   SalesInsightsAgent
   ```
2. Under **Model**, select **`gpt-4o`**.

![alt text](image.png)

---

## Step 5: Write the System Prompt

This is the most important part. The system prompt shapes how the agent reasons, what it looks for, and how it formats its output.

In the **Instructions** box, paste the following:

```
You are SalesInsightsAgent, an operational intelligence assistant for Zava Groceries.

Your job is to analyze store performance data and current news context to identify inefficiencies
and produce clear, actionable recommendations for store managers and ordering systems.

## Your Data Sources

1. **Live store data (MCP tools):** Use these to retrieve actual daily financial records
   (chickens bought, purchase costs, chickens sold, revenue, gross profit) and hourly sales
   data (chickens cooked and sold per hour). Always pull live data — never estimate.

2. **News and context (Azure AI Search):** Search for relevant news stories that may explain
   demand patterns or supply conditions. News stories cover events like supply chain disruptions,
   local weather events, and demand spikes from local events.

## What You Analyze

When asked for insights or recommendations, always examine:

- **Ordering efficiency:** What percentage of chickens bought are actually sold? Days where
  sell-through is below 70% represent waste and margin loss.
- **Cooking timing:** Using hourly data, identify which hours have the strongest and weakest
  sell-through ratios (sold ÷ cooked). Recommend shifting cook volume toward high-conversion hours.
- **Context alignment:** Cross-reference financial anomalies with news stories. A low-sales day
  that coincides with a weather event is expected; an unexplained low day warrants attention.
- **Trend direction:** Is sell-through improving or declining over the available date range?

## Output Format

Always return your analysis and recommendations in this structured markdown format:

---

## 📊 Insights Report — [Date Range] — [Store ID]

### Summary
One or two sentence summary of overall store health and the most important finding.

### Ordering Efficiency
| Date | Bought | Sold | Sell-Through % | Status |
|------|--------|------|---------------|--------|
[populate from live data]

**Finding:** [What the data shows about over/under-ordering]
**Recommendation:** [Specific adjustment to ordering volume or timing]

### Cooking Window Analysis
| Hour | Avg Cooked | Avg Sold | Conversion % | Recommendation |
|------|-----------|---------|-------------|---------------|
[populate from hourly data, grouped by hour across days]

**Finding:** [Which hours are efficient vs. wasteful]
**Recommendation:** [Specific shift in cooking schedule]

### Context & News Factors
[Summarize any relevant news stories retrieved and how they explain or inform the data patterns]

### Action Items
Numbered list of specific, concrete changes to make. Each item should include enough detail
that it could be passed to an inventory management system or another agent:

1. **[Action type]:** [Specific instruction with values — e.g., "Reduce daily order quantity
   from ~145 to ~120 units on days with no demand event signals"]
2. ...

---

Keep your analysis grounded in the data. Do not speculate beyond what the numbers and news support.
If data is missing or a tool call fails, say so explicitly rather than filling in gaps.
```

---

## Step 6: Connect Azure AI Search as a Knowledge Tool

This gives the agent access to the news stories indexed in your Azure AI Search instance.

1. In the **Tools** section, click **+ Add tool**.
2. Select **Azure AI Search** (may appear as "Grounding" or "Knowledge" depending on Foundry version).

![alt text](/docs/azure-ai-search-tool.png)

3. Select "Connect to new resource or index.

![alt text](/docs/connect_to_new_resource.png)

4. Fill in the connection details:

   | Field | Value |
   |-------|-------|
   | **Search Endpoint** | Your Azure AI Search endpoint URL from setup (e.g., `https://agenticodyssey-search-12345.search.windows.net`) |
   | **Index Name** | `news-stories` |
   | **Admin Key** | Your Azure AI Search admin key from setup |

5. Click **Save** / **Add** to confirm the knowledge source.

![alt text](/docs/connect-to-ai-search.png)

---

## Step 7: Connect the MCP Server as a Tool

Now add the live data tools from your MCP server, exactly as you did in Lab 1.

1. In the **Tools** section, click **+ Add tool** again.
2. Select **MCP Server**.
3. Enter your MCP SSE endpoint:
   ```
   http://<YOUR-IP>:8000/sse
   ```
4. Foundry will discover all 10 tools. Confirm they appear.

![alt text](/docs/all_the_tools.png)

---

## Step 8: Save the Agent

1. Click **Save** to save the configuration.
2. Note the **Agent ID** — you will need it in the orchestration lab.

![alt text](/docs/insight_agent_complete.png)

---

## Step 9: Test the Agent

### Test 1 — Full insights report
```
Analyze Store-001's performance for all available dates and give me a full insights report.
```
**Expected behavior:**
1. Agent might call `list_daily_financials` to retrieve all 10 records
2. Agent might call `list_hourly_sales` to retrieve hourly breakdown
3. Agent might search the AI Search index for relevant news stories
4. Agent returns a formatted markdown report with the ordering efficiency table, cooking window analysis, news context, and numbered action items

🤔 NOTE: Clicking on "Logs" from the result will show tool calls.

![alt text](/docs/tool_calls.png)

---

### Test 2 — News-driven analysis
```
Were there any external events that affected our sales last week? How should we adjust going forward?
```
**Expected behavior:** Agent searches AI Search for news stories, correlates them with the date-matching financial records (e.g., the storm on 2026-02-22 explains the dip), and explains the connection.

---

### Test 3 — Cooking efficiency focus
```
Which hours of the day are we wasting the most chicken? What should we change about our cooking schedule?
```
**Expected behavior:** Agent calls `list_hourly_sales` for all dates, calculates conversion rate per hour, identifies the worst-performing hours, and recommends specific shifts in cooking volume.

---

### Test 4 — Machine-readable handoff output
```
Give me the action items from your analysis in a format the inventory agent could act on.
```
**Expected behavior:** Agent returns a clean numbered list of precise, structured instructions — e.g., specific order quantity changes, specific hours to reduce cooking — suitable for passing to `ZavaGroceriesInventoryAgent` as input.

![alt text](/docs/agent_results.png)

---

## Understanding the Two-Agent Pattern

These two agents are designed to work together:

```
SalesInsightsAgent                    ZavaGroceriesInventoryAgent
─────────────────────                 ──────────────────────────
Reads data (MCP, Search)     →  Action items list  →  Executes changes (MCP CRUD)
Reasons about patterns                               Updates records
Produces recommendations                             Applies new order quantities
```

In a later lab, you will wire these together in Python so the Insights Agent's output automatically flows into the Inventory Agent as instructions, closing the loop from insight to action.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Azure AI Search tool returns no results | Verify the index name is exactly `news-stories` and documents were uploaded during setup |
| Search key rejected | Retrieve a fresh key: `az search admin-key show --service-name <name> --resource-group agenticodyssey-rg --query primaryKey -o tsv` |
| MCP tools not loading | Verify container is running: `az container show --resource-group agenticodyssey-rg --name ckriutz-mcp-server --query instanceView.state -o tsv` |
| Report missing news context | Try adding "supply chain OR weather OR demand OR Store-001" as a test search in the Foundry knowledge tool settings |
| Action items too vague | Add to your prompt: "Be specific — include exact quantities and hours" |
