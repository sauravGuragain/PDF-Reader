# vector_store.py

import faiss
import numpy as np

class VectorStore:
    def __init__(self):
        self.index = faiss.IndexFlatL2(768)  # Assuming 768-dim embeddings
        self.texts = []

    def add_vectors(self, embeddings, texts):
        embeddings = np.array(embeddings, dtype='float32')
        self.index.add(embeddings)
        self.texts.extend(texts)

    def search(self, query_embedding, k=5):
        query_embedding = np.array([query_embedding], dtype='float32')
        distances, indices = self.index.search(query_embedding, k)
        return [(self.texts[i], distances[0][j]) for j, i in enumerate(indices[0])]

# TODO: Integrate with embeddings from qa_engine
