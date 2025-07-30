from fastapi import APIRouter
from models.model import Thing
from config.database import collection
from schema.schema import list_serial
router=APIRouter()

@router.get("/")
async def get_todo():
    things=list_serial(collection.find())
    return things

@router.post("/")
async def create_todo(todo: dict):
    collection.insert_one(todo)
    return {"msg": "Todo added successfully!"}