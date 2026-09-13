# ⚙️ Decoupled Multi-Agent RAG System for Industrial Machinery Troubleshooting & K3 Compliance

## 📌 Ringkasan Proyek (Executive Summary)

**Decoupled Multi-Agent RAG System** ini adalah solusi berbasis Inteligensi Buatan (AI) cerdas yang dirancang khusus untuk membantu teknisi, *maintenance engineer*, dan operator di kawasan industri manufaktur (seperti kawasan KIIC, EJIP, dan Suryacipta di Karawang). 

Sistem ini menggabungkan teknik **Retrieval-Augmented Generation (RAG)** dengan **Arsitektur Multi-Agent**, berfungsi sebagai asisten interaktif yang dapat mendiagnosis kode kerusakan mesin secara presisi, memberikan panduan *troubleshooting* step-by-step, serta memvalidasi kepatuhan prosedur **Keselamatan dan Kesehatan Kerja (K3)** secara otomatis.

---

## 💡 Latar Belakang & Masalah yang Diselesaikan

Di lingkungan pabrik manufaktur modern, penanganan *downtime* mesin yang cepat dan aman adalah prioritas utama. Masalah yang sering dihadapi di lapangan meliputi:
1. **Dokumentasi SOP yang Tebal & Terpisah**: Manual book mesin (seperti Fanuc, Sumitomo, Komatsu, Yaskawa) sering kali dalam bentuk dokumen cetak ratusan halaman yang lambat dipahami saat situasi darurat.
2. **Risiko Kecelakaan Kerja (K3)**: Penanganan masalah teknis sering kali mengabaikan langkah keselamatan mendasar seperti penggunaan APD wajib atau prosedur *Lockout/Tagout* (LOTO).
3. **Pencarian Kata Kunci Baku**: Mesin pencari konvensional gagal memahami konteks bahasa alami teknisi di lapangan yang sering kali hanya mendeskripsikan gejala fisik kerusakan.

**Solusi Kami:** Sistem ini memproses kueri bahasa alami, melakukan *semantic search* pada vektor dokumen SOP internal, lalu menyusun jawaban yang mencakup identifikasi masalah, APD wajib, dan langkah perbaikan yang telah divalidasi oleh agen penilai keselamatan.

---

## 🎯 Fungsi Utama Sistem

1. **Pencarian Semantik Berbasis Vektor (Semantic Retrieval)**
   * Memahami maksud kueri pengguna meskipun kueri tidak menyebutkan kode error secara tepat (misalnya: hanya menyebutkan gejala *"mesin panas dan bau sangit"*).

2. **Multi-Agent Collaborative Pipeline**
   * **Router Agent**: Menganalisis kueri masuk untuk menentukan apakah pertanyaan memerlukan dokumen SOP internal (`INTERNAL_RAG`) atau obrolan umum (`GENERAL_CHAT`).
   * **Retriever Agent**: Mengambil konteks dokumen paling relevan dari database vektor ChromaDB secara *real-time*.
   * **Synthesizer Agent (LLM Engine)**: Menyusun instruksi penanganan teknis yang ringkas, berurutan, dan mudah dipahami oleh teknisi lapangan.
   * **Critic Agent (Guardrail K3)**: Bertindak sebagai pengawas keselamatan. Agen ini memeriksa jawaban dari Synthesizer untuk memastikan komponen APD dan prosedur K3 (seperti LOTO) sudah disertakan sebelum diberikan kepada pengguna.

3. **Arsitektur Decoupled (Terpisah & Skalabel)**
   * **Backend API (FastAPI)**: Menyediakan RESTful API endpoint untuk menangani seluruh komputasi AI, pencarian vektor, dan validasi agen.
   * **Frontend UI (Streamlit)**: Menyediakan antarmuka obrolan (*Chat Interface*) yang responsif dan mudah digunakan oleh operator.

---

## 🏗️ Arsitektur & Tech Stack

```text
[ User Query ]
      │
      ▼
[ Streamlit UI (Port 8501) ] ── (HTTP Request / JSON) ──► [ FastAPI Server (Port 8000) ]
                                                                   │
                                                          ┌────────┴────────┐
                                                          ▼                 ▼
                                                   [ Router Agent ]  [ General LLM ]
                                                          │
                                                (If INTERNAL_RAG)
                                                          │
                                                          ▼
                                                  [ ChromaDB Vector Store ]
                                                          │
                                                 (Context Retrieved)
                                                          │
                                                          ▼
                                                [ Synthesizer Agent ]
                                                          │
                                                          ▼
                                                  [ Critic Agent (K3) ]
                                                          │
[ Streamlit UI (Rendered Output) ] ◄── (JSON Response) ───┘
