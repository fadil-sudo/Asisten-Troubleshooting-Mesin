import streamlit as st
import requests

st.set_page_config(page_title="Asisten SOP Mesin Pabrik", page_icon="⚙️", layout="centered")

st.title("⚙️ Asisten Troubleshooting Mesin")
st.caption("Multi-Agent RAG System via FastAPI — Kawasan Industri Karawang")
st.markdown("---")

with st.form(key="query_form"):
    user_query = st.text_input("Masukkan Keluhan / Kode Error Mesin:", placeholder="Contoh: Robot las Yaskawa error ALARM 4107")
    submit_button = st.form_submit_button(label="🔍 Cari Solusi Penanganan")

if submit_button:
    if user_query.strip():
        with st.spinner("🤖 Mengirim permintaan ke server FastAPI RAG..."):
            try:
                # HIT API ke FastAPI (Port 8000)
                response = requests.post(
                    "http://localhost:8000/api/v1/chat",
                    json={"query": user_query.strip()},
                    timeout=90
                )
                
                if response.status_code == 200:
                    result = response.json()
                    text_response = result.get("answer", "")
                    
                    if result.get("route") == "INTERNAL_RAG":
                        st.success("✅ Panduan Penanganan SOP Ditemukan!")
                        with st.container(border=True):
                            st.markdown(text_response)
                        
                        critic_info = result.get("critic", {})
                        if critic_info.get("is_valid"):
                            st.info(f"🛡️ **Status Validasi K3:** {critic_info.get('note')}")
                    else:
                        st.info("ℹ️ Informasi Umum")
                        st.write(text_response)
                else:
                    st.error(f"❌ Server Error ({response.status_code}): Gagal memproses data.")
            except Exception as e:
                st.error(f"⚠️ Tidak dapat terhubung ke FastAPI server. Pastikan Uvicorn sudah berjalan di port 8000! Details: {e}")
    else:
        st.warning("⚠️ Mohon isi kode error atau gejala kerusakan mesin terlebih dahulu.")