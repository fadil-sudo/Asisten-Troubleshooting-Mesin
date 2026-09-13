# ⚙️ Multi-Agent RAG System for Industrial Machine Troubleshooting

Sistem RAG (Retrieval-Augmented Generation) berbasis Multi-Agent cerdas yang dirancang untuk membantu teknisi dan operator manufaktur (khususnya sektor industri Karawang seperti KIIC, EJIP, & Suryacipta) dalam melakukan *troubleshooting* kerusakan mesin serta penerapan standar K3 (Keselamatan dan Kesehatan Kerja).

Sistem ini dibangun dengan arsitektur **Decoupled** (backend dan frontend terpisah) yang efisien, handal, dan dapat dijalankan di lingkungan *hardware* terbatas.

---

## 🏗️ Arsitektur Sistem

Sistem ini terdiri dari dua komponen utama yang berkomunikasi melalui REST API:

1. **Backend (REST API - FastAPI)**: Port `8000`
   * **Orchestration**: Multi-Agent System (Router Agent, Retriever, Synthesizer, Critic Agent).
   * **Vector Store**: ChromaDB (Persisted Store).
   * **Embedding Model**: `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` (Local HuggingFace model).
   * **LLM Engine**: Google Gemini API (`gemini-3.6-flash`).
2. **Frontend (User Interface - Streamlit)**: Port `8501`
   * Menampilkan antarmuka obrolan interaktif untuk input kueri error/gejala mesin.
   * Menampilkan instruksi K3, APD wajib, serta solusi teknis *step-by-step*.

---

## 🛠️ Tech Stack

* **Language**: Python 3.10+
* **Backend Framework**: FastAPI, Uvicorn, Pydantic
* **Frontend Framework**: Streamlit
* **Vector Database**: ChromaDB
* **LLM & Embeddings**: Google Gemini API, Sentence-Transformers (HuggingFace)
* **Data Format**: Structured JSON Datasets (SOP Sumitomo, Komatsu, Fanuc, Yaskawa, Atlas Copco)

---

## 🚀 Fitur Utama

* 🤖 **Multi-Agent Routing**: Otomatis membedakan kueri spesifik SOP mesin internal (`INTERNAL_RAG`) dan pertanyaan umum (`GENERAL_CHAT`).
* 🛡️ **Critic Agent (K3 Validation)**: Memvalidasi bahwa setiap langkah perbaikan selalu menyertakan instruksi APD wajib dan prosedur K3 (seperti LOTO / Lockout-Tagout).
* 🔍 **Semantic Search**: Pencarian berbasis embedding vektor untuk menangkap maksud kueri pengguna meskipun menggunakan kosa kata yang bervariasi.
* ⚡ **Decoupled Architecture**: Skalabel dan siap di-deploy secara terpisah ke cloud platform.

---

## 📂 Struktur Proyek

```text
.
├── api/
│   └── main.py              # Endpoint REST API FastAPI (/api/v1/chat)
├── data/
│   └── sop_mesin.json       # Dataset SOP troubleshooting mesin manufaktur
├── src/
│   ├── graph.py             # Alur alur logika Multi-Agent (Router, Synthesizer, Critic)
│   └── ingest.py            # Script embedding & penyimpan data JSON ke ChromaDB
├── app.py                   # Aplikasi Web Frontend berbasis Streamlit
├── requirements.txt         # Daftar dependensi Python
├── .env.example             # Contoh file konfigurasi environment
└── README.md                # Dokumentasi proyek
