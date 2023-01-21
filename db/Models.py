from pydantic import BaseModel
from fastapi.params import Optional
from typing import List


class Account(BaseModel):
    id: int = -1
    username: str
    password: str
    idTracker: int = 1
    lists = []

class ListOfMissed(BaseModel):
    id: int = -1
    name: str
    idTracker: int = 1
    items: List = []

class Item(BaseModel):
    id: int = -1
    title: str
    priority: int
    links: Optional[List] = []
    description: str

class Link(BaseModel):
    URL: str