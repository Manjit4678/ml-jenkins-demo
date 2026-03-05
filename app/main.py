import os
from fastapi import FastAPI
from app.api.search_router import router
from app.core.logging_config import setup_logging
from app.services.embedding_service import EmbeddingService
from app.services.search_service import SearchService
from app.data.documents import DOCUMENTS
from app.core.config import settings

setup_logging()

app = FastAPI(title="Semantic Search API")

INDEX_PATH = "storage/faiss_index.bin"


@app.on_event("startup")
def startup_event() -> None:
    """
    Initialize embedding model and FAISS index.
    Load existing index if available, otherwise build and save.
    """
    embedding_service = EmbeddingService(settings.MODEL_NAME)

    # Get embedding dimension safely
    dimension = embedding_service.encode(["test"]).shape[1]
    search_service = SearchService(dimension)

    if os.path.exists(INDEX_PATH):
        print("Loading existing FAISS index...")
        search_service.load_index(INDEX_PATH)
    else:
        print("Creating FAISS index...")
        doc_embeddings = embedding_service.encode(DOCUMENTS)
        search_service.add_embeddings(doc_embeddings)
        search_service.save_index(INDEX_PATH)

    app.state.embedding_service = embedding_service
    app.state.search_service = search_service


@app.get("/")
def health_check() -> dict:
    return {"status": "Semantic Search API is running"}


app.include_router(router)