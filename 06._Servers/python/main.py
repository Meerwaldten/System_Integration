from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return { "message": "Welcome to our first server." }

@app.get('/firstroute')
def firstroute():
    return { "message": "Hello world from first route." }

