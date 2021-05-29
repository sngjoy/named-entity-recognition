"""
Web server for spaCy NER
"""
import json

from fastapi import FastAPI, File, HTTPException, UploadFile, status

from src.api_schemas import Entities, ModelInfo
from src.ner import SpacyNER

app = FastAPI()


@app.get("/info", response_model=ModelInfo)
async def info() -> json:
    """Returns information about the pretrained feature extractor"""

    return SpacyNER().settings


@app.post("/extract", response_model=Entities)
async def extract(file: UploadFile = File(...)) -> json:
    """Extract entities from text

    Args:
        file (UploadFile, optional): uploaded json file.

    Returns:
        json: named entities from each of the uploaded articles
    """
    if file.content_type != "application/json":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file extension. Please upload file in json format",
        )
    data_byte = await file.read()
    data = json.loads(data_byte.decode("UTF-8"))
    entities = SpacyNER.extract(data)
    return {"entities": entities}
