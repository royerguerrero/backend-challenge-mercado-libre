"""Utils"""
# Typing
from typing import List

# Models
from models import Satellite

# Utils
import math
import json


def get_satellites_online():
    satellite_coordinates = {
        'Kenobi': [-500.0, -200.0],
        'Skywalker': [100.0, -100.0],
        'Sato': [500, 100],
    }
    return satellite_coordinates


def ecludean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def get_location(distances: List[float]):
    satellite_coordinates = get_satellites_online()
    s1_x, s1_y = satellite_coordinates['Kenobi']
    s2_x, s2_y = satellite_coordinates['Skywalker']
    s3_x, s3_y = satellite_coordinates['Sato']

    s1_d = distances[0]
    s2_d = distances[1]
    s3_d = distances[2]

    # ex = pass
    # ey = pass

    i = 1
    d = 1
    j = 1

    x = (s1_d ** 2 - s2_d ** 2 + d ** 2) / 2 * d
    y = ((s1_d ** 2 + s3_d ** 2 + i ** 2 + j ** 2) / 2) - (i / j) * x
    return x, y


def get_message(messages: List[List[str]]):
    decrypted_message = {}
    for message in messages:
        for i in range(len(message)):
            if message[i] != '':
                decrypted_message[i] = message[i]

    return ' '.join(dict(sorted(decrypted_message.items())).values())


def append_satellite(satellite: Satellite):
    if satellite.name.capitalize() not in get_satellites_online().keys():
        raise Exception(f'The satellite was not found.')

    with open('storage.json', 'r+') as f:
        data = json.load(f)

        data.update({
            satellite.name: {
                "distance": satellite.distance,
                "message": satellite.message
            }
        })
        f.seek(0)
        json.dump(data, f, indent=4)
