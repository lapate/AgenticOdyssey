"""
Lab 04 — Solution: Document Ingestion into Azure AI Search
===========================================================

Reads .txt and .md files from sample_docs/, splits them into chunks,
generates embeddings via Azure OpenAI, and upserts them into an Azure
AI Search index.

Run:
    python labs/lab04-rag-agents/solution/ingest.py
"""

import hashlib
import os
import textwrap
from pathlib import Path

from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    HnswAlgorithmConfiguration,
    SearchableField,
    SearchField,
    SearchFieldDataType,
    SearchIndex,
    SimpleField,
    VectorSearch,
    VectorSearchProfile,
)
from dotenv import load_dotenv
from openai import AzureOpenAI
from rich.console import Console

load_dotenv()
console = Console()

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
SEARCH_ENDPOINT = os.environ["AZURE_SEARCH_ENDPOINT"]
SEARCH_API_KEY = os.environ["AZURE_SEARCH_API_KEY"]
INDEX_NAME = os.environ.get("AZURE_SEARCH_INDEX_NAME", "workshop-index")

AOAI_ENDPOINT = os.environ["AZURE_OPENAI_ENDPOINT"]
AOAI_API_KEY = os.environ["AZURE_OPENAI_API_KEY"]
AOAI_API_VERSION = os.environ.get("AZURE_OPENAI_API_VERSION", "2024-12-01-preview")
EMBEDDING_DEPLOYMENT = os.environ.get("AZURE_OPENAI_EMBEDDING_DEPLOYMENT", "text-embedding-3-small")
EMBEDDING_DIMENSIONS = 1536

CHUNK_SIZE = 400   # characters per chunk
CHUNK_OVERLAP = 80

SAMPLE_DOCS_DIR = Path(__file__).parent.parent / "sample_docs"

# ---------------------------------------------------------------------------
# Clients
# ---------------------------------------------------------------------------
aoai_client = AzureOpenAI(
    azure_endpoint=AOAI_ENDPOINT,
    api_key=AOAI_API_KEY,
    api_version=AOAI_API_VERSION,
)
index_client = SearchIndexClient(
    endpoint=SEARCH_ENDPOINT,
    credential=AzureKeyCredential(SEARCH_API_KEY),
)


# ---------------------------------------------------------------------------
# Index schema
# ---------------------------------------------------------------------------
def create_index() -> None:
    """Create (or recreate) the search index with vector support."""
    fields = [
        SimpleField(name="id", type=SearchFieldDataType.String, key=True),
        SimpleField(name="source", type=SearchFieldDataType.String, filterable=True),
        SearchableField(name="content", type=SearchFieldDataType.String),
        SearchField(
            name="content_vector",
            type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
            searchable=True,
            vector_search_dimensions=EMBEDDING_DIMENSIONS,
            vector_search_profile_name="hnsw-profile",
        ),
    ]

    vector_search = VectorSearch(
        algorithms=[HnswAlgorithmConfiguration(name="hnsw-algo")],
        profiles=[VectorSearchProfile(name="hnsw-profile", algorithm_configuration_name="hnsw-algo")],
    )

    index = SearchIndex(name=INDEX_NAME, fields=fields, vector_search=vector_search)
    index_client.create_or_update_index(index)
    console.print(f"[dim]Index '{INDEX_NAME}' ready.[/]")


# ---------------------------------------------------------------------------
# Chunking
# ---------------------------------------------------------------------------
def chunk_text(text: str, size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list[str]:
    """Split text into overlapping character-level chunks."""
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + size, len(text))
        chunks.append(text[start:end].strip())
        start += size - overlap
    return [c for c in chunks if c]


# ---------------------------------------------------------------------------
# Embeddings
# ---------------------------------------------------------------------------
def embed(texts: list[str]) -> list[list[float]]:
    """Generate embeddings for a list of strings."""
    response = aoai_client.embeddings.create(
        model=EMBEDDING_DEPLOYMENT,
        input=texts,
    )
    return [item.embedding for item in response.data]


# ---------------------------------------------------------------------------
# Ingestion
# ---------------------------------------------------------------------------
def ingest_file(path: Path, search_client: SearchClient) -> int:
    """Ingest a single file into the search index. Returns chunk count."""
    text = path.read_text(encoding="utf-8")
    chunks = chunk_text(text)

    embeddings = embed(chunks)

    docs = []
    for i, (chunk, vector) in enumerate(zip(chunks, embeddings)):
        doc_id = hashlib.sha256(f"{path.name}:{i}".encode()).hexdigest()[:32]
        docs.append(
            {
                "id": doc_id,
                "source": path.name,
                "content": chunk,
                "content_vector": vector,
            }
        )

    search_client.upload_documents(docs)
    return len(chunks)


def main() -> None:
    create_index()

    search_client = SearchClient(
        endpoint=SEARCH_ENDPOINT,
        index_name=INDEX_NAME,
        credential=AzureKeyCredential(SEARCH_API_KEY),
    )

    doc_files = list(SAMPLE_DOCS_DIR.glob("*.txt")) + list(SAMPLE_DOCS_DIR.glob("*.md"))
    if not doc_files:
        console.print(f"[yellow]No .txt or .md files found in {SAMPLE_DOCS_DIR}[/]")
        return

    total_chunks = 0
    for doc_path in sorted(doc_files):
        count = ingest_file(doc_path, search_client)
        console.print(f"  📄 Ingested: [cyan]{doc_path.name}[/]  →  {count} chunks")
        total_chunks += count

    console.print(f"\n✅ Index [bold]{INDEX_NAME}[/] ready with {total_chunks} documents.\n")


if __name__ == "__main__":
    main()
