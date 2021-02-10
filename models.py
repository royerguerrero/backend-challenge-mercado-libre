"""Quasar Fire Models"""
# Pydantic Models
from pydantic import BaseModel, ValidationError, validator
from typing import List, Dict

# Utils
from utils import get_satellites_online

class Satellite(BaseModel):
    name: str
    distance: float
    message: List[str]

    @validator('name')
    def find_resource_by_name(cls, name):
        if name.capitalize() not in get_satellites_online().keys():
            raise ValueError(f'The satellite with name {name} was not found.')

        return name

class Satellites(BaseModel):
    satellites: List[Satellite]

    @validator('satellites')
    def satellites_must_have_a_legth_of_three(cls, satellites):
        print(len(satellites))
        if len(satellites) != 3:
            raise ValueError('Must have a legth of three satellites.')

        return satellites


class HelpResponse(BaseModel):
    position: Dict[str, float]
    message: str