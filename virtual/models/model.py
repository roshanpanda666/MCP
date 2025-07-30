from pydantic import BaseModel

class Thing(BaseModel):
    house:str
    price:str
    year:str
    area:str