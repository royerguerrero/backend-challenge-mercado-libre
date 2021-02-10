"""Quasar Fire Models"""
# Pydantic Models
from pydantic import BaseModel
from typing import List, Dict, Optional


class Satellite(BaseModel):
    name: Optional[str]
    distance: float
    message: List[str]


class Satellites(BaseModel):
    satellites: List[Satellite] 


class HelpResponse(BaseModel):
    position: Dict[str, float]
    message: str
