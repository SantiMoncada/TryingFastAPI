from contextlib import asynccontextmanager
from dotenv import dotenv_values
from fastapi import FastAPI, Request, status, Body
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from pymongo import MongoClient
from fastapi.encoders import jsonable_encoder
from typing import List
from models import Contact


config = dotenv_values(".env")


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")
    yield
    app.mongodb_client.close()


app = FastAPI(lifespan=lifespan)

app.mount("/public", StaticFiles(directory="public"), name="public")


@app.get("/query")
async def query_params(text: str = "none"):
    return {"queryParam": text}


@app.get("/param/{path_param}")
async def path_params(path_param):
    return {"pathParam": path_param}


@app.get("/paramQuery/{path_param}")
async def path_query_params(path_param: str = "none", text: str = "none"):
    return {"message": path_param, "queryParam": text}


@app.get("/website", response_class=HTMLResponse)
async def website():
    return FileResponse("html/index.html")


@app.post(
    "/contact",
    response_description="Create a new contact",
    status_code=status.HTTP_201_CREATED,
    response_model=Contact,
)
def create_contact(request: Request, contact: Contact = Body(...)):
    contact = jsonable_encoder(contact)
    new_book = request.app.database["contacts"].insert_one(contact)
    created_book = request.app.database["contacts"].find_one(
        {"_id": new_book.inserted_id}
    )

    return created_book


@app.get(
    "/contacts", response_description="List all contacts", response_model=List[Contact]
)
def list_books(request: Request):
    contacts = list(request.app.database["contacts"].find(limit=100))
    return contacts
