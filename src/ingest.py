import json
import os
from src.database import get_troubleshooting_collection

def run_ingestion():
    file_path = os.path.join("data", "sop_mesin.json")
    
    if not os.path.exists(file_path):
        print(f"❌ File {file_path} tidak ditemukan!")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    collection = get_troubleshooting_collection()
    
    documents = []
    metadatas = []
    ids = []

    for item in data:
        text_content = f"""
        Mesin: {item['nama_mesin']}
        Kode Error: {item['kode_error']}
        Gejala: {item['gejala']}
        Penyebab: {item['penyebab']}
        Solusi: {' '.join(item['solusi_langkah_demi_langkah'])}
        APD Wajib: {', '.join(item['apd_wajib'])}
        """.strip()

        documents.append(text_content)
        metadatas.append({
            "nama_mesin": item["nama_mesin"],
            "kode_error": item["kode_error"],
            "kategori": item["kategori"],
            "tingkat_bahaya": item["tingkat_bahaya"]
        })
        ids.append(item["id"])

    collection.upsert(documents=documents, metadatas=metadatas, ids=ids)
    print(f"✅ Ingestion sukses! {len(documents)} SOP mesin tersimpan di ChromaDB.")

if __name__ == "__main__":
    run_ingestion()