import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    CHROMADB_PATH = os.getenv("CHROMADB_PATH", "./chromadb_store")
    EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

if not Config.GEMINI_API_KEY or Config.GEMINI_API_KEY == "API_KEY_GEMINI_KAMU_DISINI":
    print("⚠️ PERINGATAN: Isi GEMINI_API_KEY asli kamu di file .env terlebih dahulu!")