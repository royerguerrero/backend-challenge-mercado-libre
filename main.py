"""Quasar Fire API Rest"""

# FastAPI
from fastapi import FastAPI, Request

# Models
from models import Satellites, HelpResponse, Satellite

# Validators
from validators import satellites_must_have_a_legth_of_three, find_satellite_by_name

# Utils
from utils import get_location, get_message, SATELLITES_MEMO

app = FastAPI(title='Quasar Fire')


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
        'position': {'x': x, 'y': y, },
        'message': message
    }

    return data


@app.post('/topsecret_split/{satellite_name}')
def topsecret_split(satellite_name: str, satellite: Satellite, request: Request):
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
