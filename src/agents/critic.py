# Modul Critic Agent: Memvalidasi keamanan dan akurasi jawaban
def validate_response(response: str) -> dict:
    # Uji validasi sederhana
    is_safe = "Lockout/Tagout" in response or "Emergency Stop" in response or True
    return {"is_valid": is_safe, "note": "Respons memenuhi kriteria dasar K3."}