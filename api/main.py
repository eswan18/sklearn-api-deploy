from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def home():
    return 'the api is up and running!'
