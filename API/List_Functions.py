from API.Account_Functions import find_account

from db.db import db

def find_list(A_id: int, L_id: int):
    found = {"state": False}
    accountData = find_account(A_id)
    if accountData == False:
        return False
    else:
        for i, list in enumerate(accountData["account"].lists):
            print("The list")
            print(list)
            if list.id == L_id:
                found["state"] = True
                return {"accountIndex": accountData["index"], "index": i, "list": list}
    if found["state"] == False:
        return False

def delete_list(A_id, L_id):
    listData = find_list(A_id, L_id)
    if listData == False:
        return False
    else:
        print("AAAAAHHHHHHHHHHH")
        del db["accounts"][listData["accountIndex"]].lists[listData["index"]]
        return True

def put_list(A_id, L_id, list):
    listData = find_list(A_id, L_id)
    if listData == False:
        return False
    else:
        print("AAAAAHHHHHHHHHHH")
        list.items = db["accounts"][listData["accountIndex"]].lists[listData["index"]].items
        list.idTracker = db["accounts"][listData["accountIndex"]].lists[listData["index"]].idTracker
        list.id = db["accounts"][listData["accountIndex"]].lists[listData["index"]].id
        db["accounts"][listData["accountIndex"]].lists[listData["index"]] = list
        return True