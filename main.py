"""Quasar Fire API Rest"""

# FastAPI
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

# Models
from models import Satellites, HelpResponse, Satellite

# Validators
from validators import satellites_must_have_a_legth_of_three, find_satellite_by_name

# Utils
from utils import get_location, get_message, SATELLITES_MEMO

app = FastAPI(title='Quasar Fire')

origins = ["*"]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"],
                   allow_headers=["*"])


@app.post('/topsecret/', response_model=HelpResponse)
def top_secret(satellites: Satellites):
    """Top Secret Service: Calculates the position of the sender of
    the message based on the distance between the satellites and the
    sender and removes noise from the message."""
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
        'position': {'x': x, 'y': y, },
        'message': message
    }

    return data


@app.post('/topsecret_split/{satellite_name}')
def topsecret_split(satellite_name: str, satellite: Satellite, request: Request):
    """Top Secret Split Service: Stores the satellite data in
    the hash table [SATELLITES_MEMO] using the client's IP address"""
    find_satellite_by_name(satellite_name)
    satellite.name = satellite_name
    ip_client = request.client.host

    satellites_client = SATELLITES_MEMO.get(ip_client, None)

    if satellites_client is None:
        SATELLITES_MEMO[ip_client] = {}

    SATELLITES_MEMO[ip_client][satellite.name] = satellite
    print(SATELLITES_MEMO[ip_client])

    return {'detail': f'{satellite.name.capitalize()} satellite data added.'}


@app.get('/topsecret_split/')
def topsecret_split_read(request: Request):
    """Top Secret Split Read service: Returns the same as the
    /topscret/ service but the satellite data is extracted from the
    table up to [SATELLITES_MEMO]."""
    ip_client = request.client.host
    satellites_client = SATELLITES_MEMO.get(ip_client)

    if satellites_client is not None:
        satellites_client = list(satellites_client.values())
        print(len(satellites_client))
        if len(satellites_client) >= 3:
            SATELLITES_MEMO.pop(ip_client)
            return top_secret(Satellites(
                satellites=satellites_client))

    return {'detail': 'Not enough information.'}
