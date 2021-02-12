"""Quasar Fire Models"""
# Pydantic Models
from pydantic import BaseModel
from typing import List, Dict, Optional


class Satellite(BaseModel):
    """Handles structure each satellite."""
    name: Optional[str]
    distance: float
    message: List[str]


class Satellites(BaseModel):
    """Models the structure to payload for /topsecret/
    endpoint."""
    satellites: List[Satellite]


class HelpResponse(BaseModel):
    """Sets the response pattern to the position and message
    sent by the sender."""
    position: Dict[str, float]
    message: str
