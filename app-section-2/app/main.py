from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def status():
    return "the API is up and running!"
