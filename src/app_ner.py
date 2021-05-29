"""
Web server for spaCy NER
"""
import json

from fastapi import (Depends, FastAPI, File, HTTPException, Request,
                     UploadFile, status)
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from src.api_schemas import Entities, ModelInfo
from src.database import get_db
from src.ner import SpacyNER
from src.sql_models import EntitiesCount

app = FastAPI()
templates = Jinja2Templates(directory="src/templates")


@app.get("/")
async def index(request: Request):
    # Main page
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/info", response_model=ModelInfo)
async def info() -> json:
    """Returns information about the pretrained NER extractor"""
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


@app.post("/count", response_model=None)
async def count(file: UploadFile = File(...), db: Session = Depends(get_db)) -> json:
    """Count of the different entities of each unique news article
    and save results to postgres database

    Args:
        file (UploadFile, optional): uploaded json file.

    Returns:
        json:
    """
    if file.content_type != "application/json":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file extension. Please upload file in json format",
        )
    data_byte = await file.read()
    data = json.loads(data_byte.decode("UTF-8"))
    overall_count = SpacyNER.count(data)
    for index, all_counts in overall_count.items():
        for entity, count in all_counts.items():
            db_create = EntitiesCount(article_id=index, entities=entity, counts=count)
            db.add(db_create)
    # db.commit()
    return {"success": True}
