# FastAPI
from fastapi import FastAPI
from typing import Dict, List

# Models
from models import Satellite, HelpResponse

# Utils
from utils import get_location, get_message

app = FastAPI()


@app.post('/top_secret/', response_model=HelpResponse)
def top_secret(satellites: Dict[str, List[Satellite]]):
    print(satellites)
    for satellite in satellites:
        print(satellite)

    return {"Hello": "World"}