"""Utils"""
from typing import List
import math


def get_satellites_online():
    satellite_coordinates = {
        'Kenobi': [-500.0, -200.0],
        'Skywalker': [100.0, -100.0],
        'Sato': [500, 100],
    }
    return satellite_coordinates


def get_location(distances: List[float]):
    satellite_coordinates = get_satellites_online()
    s1_x, s1_y = satellite_coordinates['Kenobi']
    s2_x, s2_y = satellite_coordinates['Skywalker']
    s3_x, s3_y = satellite_coordinates['Sato']

    s1_d = distances[0]
    s2_d = distances[1]
    s3_d = distances[2]

    i = math.sqrt((s3_x - s1_x)**2 + (s3_y - s1_y)**2)
    d = math.sqrt((s2_x - s1_x)**2 + (s2_y - s1_y)**2)
    j = math.sqrt((s3_x - s2_x)**2 + (s3_y - s2_y)**2)

    x = (s1_d**2 - s2_d**2 + d**2) / 2 * d
    y = ((s1_d**2 + s3_d**2 + i**2 + j**2) / 2) - (i / j) * x
    return x, y


def get_message(messages: List[str]):
    message = []
    for i in messages:
        if i not in message and i != "":
            message.append(i)

    return ' '.join(message)


d = [100.0, 115.5, 142.7]
print(get_location(d))