import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

CHUNK_SIZE = 500

def create_chunks(text):
    chunks = []
    for i in range(0, len(text), CHUNK_SIZE):
        chunks.append(text[i:i+CHUNK_SIZE])
    return chunks

def build_faiss_index(chunks):
    embeddings = model.encode(chunks)
    embeddings = np.array(embeddings).astype("float32")
    
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    return index, chunks

def search(query, index, chunks, top_k=3):
    query_embed = model.encode([query]).astype("float32")
    distances, indices = index.search(query_embed, top_k)
    
    results = [chunks[i] for i in indices[0]]
    return results
