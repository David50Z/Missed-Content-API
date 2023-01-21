from API.List_Functions import find_list
from db.db import db

def find_item(A_id, L_id, T_id):
    data = find_list(A_id, L_id)
    found = {"state": False}

    print("DATAAAAAAAAA")
    print(data)
    print(A_id, L_id, T_id)

    if data == False:
        return False
    else:
        for i, item in enumerate(data["list"].items):
            print("The item")
            print(item)
            print(type(item.id))
            print(type(T_id))
            if item.id == T_id:
                print('THING WAS FOOOOOOOUUUUUND')
                found["state"] = True
                return {
                "accountIndex": data["accountIndex"], 
                "listIndex": data["index"], 
                "index": i,
                "item": item}
    if found["state"] == False:
        return False

def create_item(A_id, L_id, item):
    data = find_list(A_id, L_id)

    if data == False:
        return False
    else:
        item.id = data["list"].idTracker
        db["accounts"][data["accountIndex"]].lists[data["index"]].idTracker += 1
        db["accounts"][data["accountIndex"]].lists[data["index"]].items.append(item)
        return db["accounts"][data["accountIndex"]].lists[data["index"]]

def put_item(A_id, L_id, T_id, item):
    data = find_item(A_id, L_id, T_id)
    if data == False:
        return False
    else:
        print("AAAAAHHHHHHHHHHH")
        item.links = db["accounts"][data["accountIndex"]].lists[data["listIndex"]].items[data["index"]].links
        db["accounts"][data["accountIndex"]].lists[data["listIndex"]].items[data["index"]] = item
        db["accounts"][data["accountIndex"]].lists[data["listIndex"]].items[data["index"]].id = int(T_id)
        return True

def delete_item(A_id, L_id, T_id):
    data = find_item(A_id, L_id, T_id)
    if data == False:
        return False
    else:
        print("AAAAAHHHHHHHHHHH")
        del db["accounts"][data["accountIndex"]].lists[data["listIndex"]].items[data["index"]]
        return True

## LINKS CRUD

def create_link(A_id, L_id, T_id, link):
    data = find_item(A_id, L_id, T_id)

    print("DATAAAAAAAAA")
    print(A_id, L_id, T_id)

    if data == False:
        return False
    else:
        db["accounts"][data["accountIndex"]].lists[data["listIndex"]].items[data["index"]].links.append(link.URL)
        return db["accounts"][data["accountIndex"]].lists[data["listIndex"]].items[data["index"]]

def delete_link(A_id, L_id, T_id, link):
    data = find_item(A_id, L_id, T_id)
    found = {"state": False}

    if data == False:
        return False
    else:
        for i, url in enumerate(db["accounts"][data["accountIndex"]].lists[data["listIndex"]].items[data["index"]].links):
            if url == link.URL:
                del db["accounts"][data["accountIndex"]].lists[data["listIndex"]].items[data["index"]].links[i]
                found["state"] = True
    if found["state"] == True and data != False:
        return True
    else:
        return False