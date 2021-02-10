from fastapi import FastAPI

app = FastAPI()


@app.post("/top_secret/")
def top_secret():
    return {"Hello": "World"}