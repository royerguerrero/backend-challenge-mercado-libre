"""Utils"""
# Typing
from typing import List

SATELLITES_MEMO = {}


def get_satellites_online():
    satellite_coordinates = {
        'Kenobi': [-500.0, -200.0],
        'Skywalker': [100.0, -100.0],
        'Sato': [500.0, 100.0],
    }
    return satellite_coordinates


def get_location(distances: List[float]):
    satellite_coordinates = get_satellites_online()
    x1, y1 = satellite_coordinates['Kenobi']
    x2, y2 = satellite_coordinates['Skywalker']
    x3, y3 = satellite_coordinates['Sato']

    r1 = distances[0]
    r2 = distances[1]
    r3 = distances[2]

    A = 2 * x2 - 2 * x1
    B = 2 * y2 - 2 * y1
    C = r1 ** 2 - r2 ** 2 - x1 ** 2 + x2 ** 2 - y1 ** 2 + y2 ** 2
    D = 2 * x3 - 2 * x2
    E = 2 * y3 - 2 * y2
    F = r2 ** 2 - r3 ** 2 - x2 ** 2 + x3 ** 2 - y2 ** 2 + y3 ** 2
    x = (C * E - F * B) / (E * A - B * D)
    y = (C * D - A * F) / (B * D - A * E)

    return x, y


def get_message(messages: List[List[str]]):
    decrypted_message = {}
    for message in messages:
        for i in range(len(message)):
            if message[i] != '':
                decrypted_message[i] = message[i]

    return ' '.join(dict(sorted(decrypted_message.items())).values())
