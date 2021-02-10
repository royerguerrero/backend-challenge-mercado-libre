"""Quasar Fire Models"""
from pydantic import BaseModel
from typing import List, Dict


class Satellite(BaseModel):
    name: str
    distance: float
    message: List[str]


class HelpResponse(BaseModel):
    position: Dict[str, float]
    message: str