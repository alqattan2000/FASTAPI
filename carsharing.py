from fastapi import FastAPI,Request
from datetime import datetime

app = FastAPI()

@app.get("/")
def welcome():
    """ Return a friendly Welcome Message. """
    return {'message':"welcome to the Car Sharing Service!"}

@app.get("/date")
def date(request: Request):
    """return system date"""
    client_host = request.client.host  + ":"+  str(request.client.port)
    print(client_host)
    return {'date': datetime.now()}