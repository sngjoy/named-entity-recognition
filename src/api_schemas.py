# pylint: skip-file
"""
Define schemas for API input/output
"""
from typing import Dict, List, Tuple

from pydantic import BaseModel


class Entities(BaseModel):
    entities: Dict[str, List[Tuple[str, str]]]


class ModelInfo(BaseModel):
    nlp_library: str
    model_name: str
