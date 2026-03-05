import faiss
import numpy as np
import os


class SearchService:
    def __init__(self, dimension: int):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(self.dimension)

    def add_embeddings(self, embeddings: np.ndarray) -> None:
        self.index.add(embeddings)

    def search(self, query_embedding: np.ndarray, top_k: int):
        distances, indices = self.index.search(query_embedding, top_k)
        return distances, indices

    def save_index(self, path: str) -> None:
        faiss.write_index(self.index, path)

    def load_index(self, path: str) -> None:
        self.index = faiss.read_index(path)