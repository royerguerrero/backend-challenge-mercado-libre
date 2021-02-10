"""Quasar Fire Validators"""

# FastAPI
from fastapi import status, HTTPException

# Utils
from utils import get_satellites_online


def satellites_must_have_a_legth_of_three(satellites):
    if len(satellites) != 3:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

def find_satellite_by_name(name):
    if name.capitalize() not in get_satellites_online().keys():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)