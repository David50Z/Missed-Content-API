from db.db import db

def delete_account(id):
    print("This is the Id")
    print(id)
    data = find_account(id)
    if data == False:
        return False
    else:
        del db["accounts"][find_account(id)["index"]]
        return True

def find_account(id):
    found = {"state": False}
    for i, account in enumerate(db["accounts"]):
        print("The account")
        print(account)
        if account.id == id:
            found["state"] = True
            return {"index": i, "account": account}
    if found["state"] == False:
        return False

def put_account(id, account):
    accountData = find_account(id)
    if accountData == False:
        return False
    else:
        print("AAAAAHHHHHHHHHHH")
        print(db["accounts"][accountData["index"]])
        account.idTracker = db["accounts"][accountData["index"]].idTracker
        account.lists = db["accounts"][accountData["index"]].lists
        account.id = db["accounts"][accountData["index"]].id
        db["accounts"][accountData["index"]] = account
        db["accounts"][accountData["index"]].id = int(id)
        return True