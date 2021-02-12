<h1 align="center">💫 Operacion Quasar Fire 🚀</h1>

## Requirements ⏬

- python3
- pip3
- venv

## Run development environment 🛠️
To install this application for development you must meet the above requirements.

1. Create a virtual environment using `python -m venv .env`

2. Activates the virtual environment by running \
   UNIX: `source .env/bin/activate`  WIN: `source .env/Scripts/activate`

3. Download all dependencies with `pip install -r requirements.txt`
4. Run development server using `uvicorn main:app --reload`
5. Go to [127.0.0.1:8000](http://127.0.0.1:8000/)

## Run tests 🏃
For run the test you can use `pytest -v tests.py`

## Services 🌐
- POST -> `/topsecret/`
  - Payload Schema
    ```
    {
      "satellites": [
        {
          "name": "s1",
          "distance": 10.0,
          "message": ["hello", "", "!!!"]
       },
        ...
      ]
    }
    ```
- POST -> `/topsecret_split/{satellite_name}/`
  - Payload Schema
    ```
    {
      "name": "s2",
      "distance": 80.0,
      "message": ["", "world", "everybody"]
    }
    ```
- GET -> `/topsecret_split/`    