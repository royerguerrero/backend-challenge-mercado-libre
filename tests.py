"""Quasar Fire Test"""

# FastAPI
from fastapi.testclient import TestClient

# App
from main import app

client = TestClient(app)


def test_topsecret_endpoint():
    payload = {
        'satellites': [
            {
                'name': 'kenobi',
                'distance': 222,
                'message': [
                    'este', '', '', 'mensaje', ''
                ]
            },
            {
                'name': 'skywalker',
                'distance': 88.5,
                'message': [
                    '', 'es', '', '', 'secreto'
                ]
            },
            {
                'name': 'sato',
                'distance': 78.4,
                'message': [
                    'este', '', 'un', '', ''
                ]
            }
        ]
    }
    response = client.post('/topsecret/', json=payload)
    assert response.status_code == 200
    assert response.json()['position']['x'] == -436.73886875
    assert response.json()['position']['y'] == 1477.6919625
    assert response.json()['message'] == 'este es un mensaje secreto'


def test_topsecret_split():
    payloads = [
        {
            'name': 'sato',
            'distance': 101.2,
            'message': ['hello', '', 'mercadolibre', '']
        },
        {
            'name': 'skywalker',
            'distance': 87.0,
            'message': ['', 'world', '', '!!!']
        },
        {
            'name': 'kenobi',
            'distance': 225,
            'message': ['', '', 'mercadolibre', '!!!']
        }
    ]

    for i in payloads:
        name = i['name']
        i.pop('name')
        response = client.post(f'/topsecret_split/{name}', json=i)
        assert response.status_code == 200
        assert response.json()['detail'] == f'{name.capitalize()} satellite data added.'

    response = client.get('/topsecret_split/')
    print(response.json())
    assert response.json()['position']['x'] == -457.24945
    assert response.json()['position']['y'] == 1406.8589
    assert response.json()['message'] == 'hello world mercadolibre !!!'
