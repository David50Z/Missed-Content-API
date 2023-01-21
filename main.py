from fastapi import FastAPI
from fastapi.params import Body
from fastapi.params import Optional
from pydantic import BaseModel

from typing import List

from db.Models import Account
from db.Models import ListOfMissed
from db.Models import Item
from db.Models import Link
from db.db import db

from API.Account_Functions import find_account
from API.Account_Functions import delete_account
from API.Account_Functions import put_account

from API.List_Functions import find_list
from API.List_Functions import put_list
from API.List_Functions import delete_list

from API.Item_Functions import find_item
from API.Item_Functions import create_item
from API.Item_Functions import put_item
from API.Item_Functions import delete_item

from API.Item_Functions import create_link
from API.Item_Functions import delete_link

import requests

app = FastAPI()

id = []

data = {
    "id": 1,
    "username": "David50Z",
    "password": "rod23",
    "over18": True,
    "premAccount": False,
    "idTracker": 2,
    "lists": [
        {
            "id": 1,
            "name": "Anime",
            "idTracker": 1,
            "items": []
        }
    ]
}


@app.get("/")
async def root():
    return {"data": db}

@app.get("/{id}")
def find_account_path(id: int):
    data = find_account(id)
    if data == False:
        raise Exception("Account not found")
    else:
        return data["account"]

@app.post("/")
def create_account_path(new_account: Account):
    db["idTracker"]+= 1
    new_account.id = db["idTracker"]
    new_account.lists = []
    new_account.idTracker = 1
    db["accounts"].append(new_account)
    return {"data": db["accounts"], "id": db["idTracker"]}

@app.delete("/{id}")
def delete_account_path(id: int):
    print("this is the type")
    print(type(id))
    data = delete_account(id)
    if data == False :
        raise Exception("account not found")
    else:
        return {"data": db["accounts"]}

@app.put("/{id}")
def put_account_path(id: int, account: Account):
    data = put_account(id, account)
    if data == False:
        raise Exception("account not found")
    else:
        return db["accounts"]


## LIST CRUD

@app.get("/{A_id}/{L_id}")
def find_list_path(A_id: int, L_id: int):
    data = find_list(A_id, L_id)
    if data == False:
        raise Exception("List not found")
    else:
        return data["list"]

@app.post("/{id}")
def create_list_path(id: int, list: ListOfMissed):
    data = find_account(id)
    list.id = db["accounts"][data["index"]].idTracker
    list.idTracker = 1
    list.items = []
    db["accounts"][data["index"]].idTracker += 1
    print("TEEEEEEEEEEEEESSSSSSSSSSSTTTTTTTTTTT")
    print(db["accounts"][data["index"]])
    db["accounts"][data["index"]].lists.append(list)
    return db["accounts"][data["index"]]

@app.put("/{A_id}/{L_id}")
def put_list_path(A_id: int, L_id: int, list: ListOfMissed):
    data = put_list(A_id, L_id, list)
    if data == False:
        raise Exception("Data not found")
    else:
        return find_account(A_id)

@app.delete("/{A_id}/{L_id}")
def delete_list_path(A_id: int, L_id: int):
    data = delete_list(A_id, L_id)
    if data == False:
        raise Exception("Data not found")
    else:
        return find_account(A_id)["account"].lists

## ITEM CRUD

@app.get("/{A_id}/{L_id}/{T_id}")
def get_item_path(A_id: int, L_id: int, T_id: int):
    data = find_item(A_id, L_id, T_id)

    if data == False:
        raise Exception("Data not found")
    else:
        return data["item"]

@app.post("/{A_id}/{L_id}")
def create_item_path(A_id: int, L_id: int, item: Item):
    data = create_item(A_id, L_id, item)

    if data == False:
        raise Exception("Data not found")
    else:
        return data

@app.put("/{A_id}/{L_id}/{T_id}")
def put_item_path(A_id: int, L_id: int, T_id: int, item: Item):
    data = put_item(A_id, L_id, T_id, item)
    if data == False:
        raise Exception("Data not found")
    else:
        return find_list(A_id, L_id)

@app.delete("/{A_id}/{L_id}/{T_id}")
def delete_list_path(A_id: int, L_id: int, T_id: int):
    data = delete_item(A_id, L_id, T_id)
    if data == False:
        raise Exception("Data not found")
    else:
        return find_list(A_id, L_id)

## LINK CRUD

@app.post("/links/{A_id}/{L_id}/{T_id}")
def create_link_path(A_id: int, L_id: int, T_id: int, link: Link):
    data = create_link(A_id, L_id, T_id, link)

    if data == False:
        raise Exception("Data not found")
    else:
        return data

@app.delete("/links/{A_id}/{L_id}/{T_id}")
def delete_link_path(A_id: int, L_id: int, T_id: int, link: Link):
    data = delete_link(A_id, L_id, T_id, link)
    if data == False:
        raise Exception("Data not found")
    else:
        return find_list(A_id, L_id)