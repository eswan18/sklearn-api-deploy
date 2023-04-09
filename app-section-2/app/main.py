from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def status():
    """Check that the API is working."""
    return "the API is up and running!"
