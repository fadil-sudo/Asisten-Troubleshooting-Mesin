from langchain_google_genai import ChatGoogleGenerativeAI
from src.config import Config

def route_query(user_query: str) -> str:
    llm = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        google_api_key=Config.GEMINI_API_KEY,
        temperature=0.0
    )
    
    prompt = f"""
    Analisis kueri pengguna berikut. Jika kueri berkaitan dengan kerusakan mesin, kode error, SOP maintenance, atau keluhan teknis pabrik, jawab HANYA dengan kata 'INTERNAL_RAG'. 
    Jika kueri adalah sapaan atau pertanyaan umum, jawab HANYA dengan kata 'GENERAL_CHAT'.

    Kueri: {user_query}
    Keputusan:
    """
    
    response = llm.invoke(prompt)
    
    content_text = str(response.content) if isinstance(response.content, list) else response.content
    decision = content_text.strip()
    return "INTERNAL_RAG" if "INTERNAL_RAG" in decision else "GENERAL_CHAT"