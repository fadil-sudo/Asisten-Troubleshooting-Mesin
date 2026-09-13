from langchain_google_genai import ChatGoogleGenerativeAI
from src.config import Config

def synthesize_answer(query: str, context_docs: list) -> str:
    if not context_docs:
        return "Mohon maaf, tidak ditemukan SOP yang relevan untuk keluhan tersebut di database."

    # Update nama model ke versi terbaru
    llm = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        google_api_key=Config.GEMINI_API_KEY,
        temperature=0.2
    )

    context_text = "\n\n".join(context_docs)

    prompt = f"""
    Kamu adalah pakar teknisi mesin manufaktur. Tugasmu adalah menjawab keluhan teknisi berdasarkan SOP yang diberikan.
    
    KRITERIA PENTING:
    - Hanya gunakan informasi dari Dokumen SOP di bawah ini yang RELEVAN dengan kueri pengguna.
    - Jika ada dokumen yang tidak berhubungan dengan keluhan pengguna, ABAIKAN dokumen tersebut.
    - Buat jawaban yang rapi, berurut, dan sertakan APD Wajib serta langkah K3 secara tegas.

    [Dokumen SOP]:
    {context_text}

    [Kueri Pengguna]:
    {query}

    Jawaban:
    """

    response = llm.invoke(prompt)
    return response.content