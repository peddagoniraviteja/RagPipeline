import openai
from app.embedding import embedding_model, chunk_text

openai.api_key = 'your-openai-api-key'

def generate_response(retrieved_chunks, query):
    context = '\n'.join(retrieved_chunks)
    prompt = f"Use the following context to answer the question:\n\nContext:\n{context}\n\nQuestion: {query}\n\nAnswer:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        temperature=0
    )
    return response['choices'][0]['text'].strip()
