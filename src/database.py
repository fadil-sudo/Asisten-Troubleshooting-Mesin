import streamlit as st
import chromadb
from chromadb.utils import embedding_functions
from src.config import Config

# Gunakan @st.cache_resource agar model embedding di-load SEKALI SAJA ke RAM
@st.cache_resource
def get_embedding_function():
    return embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=Config.EMBEDDING_MODEL
    )

# Cache juga instance koneksi ChromaDB
@st.cache_resource
def get_chroma_client():
    return chromadb.PersistentClient(path=Config.CHROMADB_PATH)

def get_troubleshooting_collection():
    embedding_fn = get_embedding_function()
    chroma_client = get_chroma_client()
    
    return chroma_client.get_or_create_collection(
        name="troubleshooting_mesin",
        embedding_function=embedding_fn
    )