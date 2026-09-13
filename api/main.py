from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from src.graph import run_multiagent_pipeline

app = FastAPI(
    title="RAG Multi-Agent Troubleshooting API",
    description="REST API Asisten Penanganan Kerusakan Mesin Manufaktur",
    version="1.0.0"
)

# Izinkan komunikasi antar-service (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str = Field(..., example="Robot las Yaskawa error ALARM 4107")

@app.get("/", tags=["Health Check"])
def root():
    return {"message": "API RAG Multi-Agent Troubleshooting Mesin Aktif!"}

@app.post("/api/v1/chat", tags=["Troubleshooting Chat"])
def chat_endpoint(request: QueryRequest):
    if not request.query.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Kueri tidak boleh kosong."
        )
    try:
        result = run_multiagent_pipeline(request.query)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Terjadi kesalahan pada pipeline agen: {str(e)}"
        )