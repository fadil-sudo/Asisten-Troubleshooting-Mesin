from src.database import get_troubleshooting_collection

def retrieve_docs(query: str, n_results: int = 2):
    collection = get_troubleshooting_collection()
    results = collection.query(query_texts=[query], n_results=n_results)
    return results["documents"][0] if results["documents"] else []