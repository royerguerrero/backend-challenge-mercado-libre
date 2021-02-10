# FastAPI
from fastapi import FastAPI
from typing import Dict, List

# Models
from models import Satellites, HelpResponse

# Utils
from utils import get_location, get_message

app = FastAPI()


@app.post('/top_secret/')
def top_secret(satellites: Satellites):
    satellites = satellites.satellites
    dirt_message = []
    distances = []

    for satellite in satellites:
        dirt_message += satellite.message
        distances.append(satellite.distance)

    print(distances)
    # x, y = get_message(distances)
    data = {
        'position': {
            'x': 0,
            'y': 1,
        },
        'message': get_message(dirt_message)
    }

    return data

