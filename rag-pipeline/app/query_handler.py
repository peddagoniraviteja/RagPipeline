def query_to_vector(query):
    query_embedding = embedding_model.encode([query])
    distances, indices = index.search(query_embedding, k=5)  # Top 5 matches
    return distances, indices

def fetch_chunks_by_indices(indices, all_chunks):
    return [all_chunks[i] for i in indices[0]]
