from fastapi import APIRouter, Request
from app.models.request_models import SearchRequest
from app.data.documents import DOCUMENTS
from app.core.config import settings

router = APIRouter()


@router.post("/search")
def search(request: SearchRequest, req: Request) -> dict:
    """
    Perform semantic search over documents.
    """
    embedding_service = req.app.state.embedding_service
    search_service = req.app.state.search_service

    query_embedding = embedding_service.encode([request.query])
    distances, indices = search_service.search(
        query_embedding,
        settings.TOP_K
    )

    results = [
        {
            "text": DOCUMENTS[i],
            "score": float(distances[0][idx])
        }
        for idx, i in enumerate(indices[0])
    ]

    return {"results": results}