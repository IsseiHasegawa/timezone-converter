from fastapi import FastAPI
from app.schemas import ConvertRequest, ConvertResponse
from app.services.converter import convert_times

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is running"}

@app.post("/convert", response_model=ConvertResponse)
def convert(req: ConvertRequest):
    results = convert_times(req.from_timezone, req.to_timezone, req.times)
    return {"results" : results}