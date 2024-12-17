from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
dimension = 384
index = faiss.IndexFlatL2(dimension)

def chunk_text(text, max_chunk_size=300):
    sentences = text.split('\n')
    chunks = []
    chunk = ''
    for sentence in sentences:
        if len(chunk) + len(sentence) <= max_chunk_size:
            chunk += ' ' + sentence
        else:
            chunks.append(chunk.strip())
            chunk = sentence
    if chunk:
        chunks.append(chunk.strip())
    return chunks

def embed_and_store(chunks):
    embeddings = embedding_model.encode(chunks)
    index.add(np.array(embeddings))
    return embeddings
