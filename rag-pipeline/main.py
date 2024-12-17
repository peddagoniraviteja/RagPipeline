from fastapi import FastAPI, UploadFile, Form
from app.ingestion import extract_text_from_pdf
from app.embedding import chunk_text, embed_and_store
from app.query_handler import query_to_vector, fetch_chunks_by_indices
from app.response_generation import generate_response

app = FastAPI()
all_chunks = []

@app.post("/upload_pdf/")
async def upload_pdf(file: UploadFile):
    file_path = f"./data/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    content = extract_text_from_pdf(file_path)
    chunks = chunk_text('\n'.join(content))
    embed_and_store(chunks)
    all_chunks.extend(chunks)  # Store for use in queries
    return {"message": "PDF processed successfully."}

@app.post("/query/")
async def query_pdf(question: str):
    distances, indices = query_to_vector(question)
    relevant_chunks = fetch_chunks_by_indices(indices, all_chunks)
    response = generate_response(relevant_chunks, question)
    return {"response": response}
@app.get("/")
def read_root():
    return {"message": "Welcome to the RAG pipeline!"}