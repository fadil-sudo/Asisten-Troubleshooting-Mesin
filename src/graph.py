from src.agents.router import route_query
from src.agents.retriever import retrieve_docs
from src.agents.synthesizer import synthesize_answer
from src.agents.critic import validate_response

def run_multiagent_pipeline(user_query: str) -> dict:
    route = route_query(user_query)
    
    if route == "INTERNAL_RAG":
        docs = retrieve_docs(user_query)
        raw_answer = synthesize_answer(user_query, docs)
        
        # PERBAIKAN: Pastikan output answer berupa string murni agar Streamlit rapi
        if isinstance(raw_answer, list):
            # Jika Gemini mengembalikan list of dicts/text
            clean_answer = "".join([item.get("text", str(item)) if isinstance(item, dict) else str(item) for item in raw_answer])
        else:
            clean_answer = str(raw_answer)
            
        critic_check = validate_response(clean_answer)
        
        return {
            "query": user_query,
            "route": route,
            "answer": clean_answer,
            "critic": critic_check
        }
    else:
        return {
            "query": user_query,
            "route": route,
            "answer": "Halo! Saya adalah Asisten AI Troubleshooting Mesin. Silakan tanyakan kode error atau keluhan mesin pabrik Anda.",
            "critic": {"is_valid": True, "note": "Pertanyaan Umum"}
        }