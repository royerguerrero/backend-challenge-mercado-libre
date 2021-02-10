# FastAPI
from fastapi import FastAPI, status, Body
from fastapi.responses import JSONResponse
from typing import List

# Models
from models import Satellites, HelpResponse, Satellite

# Utils
from utils import get_location, get_message

# Validators
from validators import satellites_must_have_a_legth_of_three, find_satellite_by_name

app = FastAPI()


@app.post('/topsecret/', response_model=HelpResponse)
def top_secret(satellites: Satellites):
    satellites = satellites.satellites
    dirt_message = []
    distances = []

    satellites_must_have_a_legth_of_three(satellites)

    for satellite in satellites:
        find_satellite_by_name(satellite.name)
        dirt_message.append(satellite.message)
        distances.append(satellite.distance)

    x, y = get_location(distances)
    
    message = get_message(dirt_message)

    data = {
        'position': {'x': x, 'y': y,},
        'message': message
    }

    return data

@app.post('/topsecret_split/{satellite_name}')
def topsecret_split(satellite_name: str, satellite: Satellite):
    find_satellite_by_name(satellite_name)
    satellite.name = satellite_name

    return {'Works...': 1}