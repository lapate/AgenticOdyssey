# Lab 04: RAG-Powered Agents

## Overview

In this lab you will build a **Retrieval-Augmented Generation (RAG)** agent that answers questions grounded in your own documents. You'll index documents into **Azure AI Search**, then wire the search index as a tool that an Azure OpenAI agent calls on every turn — giving you a fully grounded, citation-aware assistant.

**Duration:** ~45 minutes

---

## Learning Objectives

By the end of this lab you will be able to:

1. Explain how RAG extends an LLM with external knowledge
2. Ingest documents into an Azure AI Search index with vector embeddings
3. Implement a `search_documents` tool that queries the index
4. Build an agent that cites sources from the index in every answer
5. Evaluate grounding quality by checking citations against source documents

---

## Prerequisites

- Completed [Lab 02](../lab02-first-agent/README.md)
- Azure AI Search resource created (see setup below)
- `.env` configured with `AZURE_SEARCH_*` variables
- Azure OpenAI with an **embeddings** deployment (e.g. `text-embedding-ada-002` or `text-embedding-3-small`)

---

## Azure AI Search Setup

1. In the [Azure Portal](https://portal.azure.com), search for **Azure AI Search** and create a new resource:
   - **Name:** `srch-agentic-odyssey-<suffix>`
   - **Pricing tier:** Free (for the workshop) or Basic
2. Once created, go to **Keys** and copy the **Admin key**
3. Copy the **URL** from the Overview page
4. Add to your `.env`:
   ```dotenv
   AZURE_SEARCH_ENDPOINT=https://<your-service>.search.windows.net
   AZURE_SEARCH_API_KEY=<admin-key>
   AZURE_SEARCH_INDEX_NAME=workshop-index
   ```
5. Add an embeddings deployment to your Azure OpenAI resource:
   - Model: `text-embedding-3-small`, deployment name: `text-embedding-3-small`
   - Add to `.env`: `AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-small`

---

## Step 1: Ingest Sample Documents

Run the ingestion script to create the index and upload the sample documents included in this lab:

```bash
cd labs/lab04-rag-agents
python solution/ingest.py
```

Expected output:

```
📄 Ingesting: sample_docs/azure_openai_overview.txt    ✅  5 chunks
📄 Ingesting: sample_docs/autogen_overview.txt         ✅  4 chunks
📄 Ingesting: sample_docs/semantic_kernel_overview.txt ✅  4 chunks
✅ Index 'workshop-index' ready with 13 documents.
```

---

## Step 2: Run the RAG Agent

```bash
python solution/rag_agent.py
```

Ask the agent a question about one of the ingested documents:

```
You: What is Azure OpenAI and what models does it provide?
You: How does AutoGen handle multi-agent conversations?
You: What programming languages does Semantic Kernel support?
```

Observe that the agent:
1. Calls `search_documents` with a semantic query
2. Receives relevant chunks with source filenames
3. Cites the sources in its final answer

---

## Step 3: Ingest Your Own Documents

1. Drop any `.txt` or `.md` files into `labs/lab04-rag-agents/sample_docs/`
2. Re-run `python solution/ingest.py`
3. Ask the RAG agent questions about your documents

---

## Step 4: Tune Retrieval (Starter Exercise)

Open `starter/rag_agent.py`. The `search_documents` function currently uses **keyword search**. Upgrade it to use **hybrid search** (keyword + vector):

```python
# TODO: Change search_type to "semantic" or hybrid
# Hint: Azure AI Search supports:
#   search_type="simple"   — BM25 keyword search
#   search_type="semantic" — semantic re-ranking (requires semantic config)
#   vector_queries=[...]   — pure vector search
#   (combine vector_queries + search_text for hybrid)
```

Compare result quality before and after the change.

---

## Key Takeaways

| Concept | Description |
|---------|-------------|
| **Chunking** | Split documents into passages that fit in the context window |
| **Embedding** | Dense vector representation of text for semantic search |
| **Hybrid search** | BM25 + vector search for best recall and precision |
| **Grounding** | Agent answers based on retrieved context, reducing hallucination |
| **Citations** | Include source filenames so users can verify answers |

---

## Next Steps

You've completed all four labs! Head to the **[Demos](../../demos/)** to see these concepts applied in full end-to-end scenarios.
