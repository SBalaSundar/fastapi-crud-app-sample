# main.py
# Import FastAPI
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import api

# Initialize the app
app = FastAPI()

app.include_router(api.router)


# GET operation at route '/'
@app.get('/')
def root_api():
    return {"message": "Welcome to Balasundar's Technical Blog"}
