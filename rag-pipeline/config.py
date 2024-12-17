import os
from dotenv import load_dotenv

# Load environment variables from a .env file (if exists)
load_dotenv()

# Application Configurations
APP_NAME = "Chat with PDF RAG Pipeline"
VERSION = "1.0.0"

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "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")

# File Paths
DATA_FOLDER = "./data"
EMBEDDINGS_FOLDER = "./embeddings"

# Embedding Model Configurations
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
EMBEDDING_DIMENSION = 384

# FastAPI Server Configurations
HOST = "0.0.0.0"
PORT = 8000

# Vector Database Config
TOP_K_RESULTS = 5  # Number of most similar chunks to retrieve
