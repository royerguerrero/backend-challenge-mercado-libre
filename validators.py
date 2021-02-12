"""Quasar Fire Validators"""

# FastAPI
from fastapi import status, HTTPException

# Utils
from utils import get_satellites_online


def satellites_must_have_a_legth_of_three(satellites):
    """Validates that satellites object are 3."""
    if len(satellites) != 3:
        raise HTTPException(detail={'RESPONSE CODE': 404},
                            status_code=status.HTTP_404_NOT_FOUND)


def find_satellite_by_name(name):
    """Checks that satellite is online."""
    if name.capitalize() not in get_satellites_online().keys():
        raise HTTPException(detail={'RESPONSE CODE': 404},
                            status_code=status.HTTP_404_NOT_FOUND)
