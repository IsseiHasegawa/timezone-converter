from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import ConvertRequest, ConvertResponse
from app.services.converter import convert_times

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # ← ★これを追加
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "API is running"}

@app.post("/convert", response_model=ConvertResponse)
def convert(req: ConvertRequest):
    results = convert_times(req.from_timezone, req.to_timezone, req.times)
    return {"results": results}