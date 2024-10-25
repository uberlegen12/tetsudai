import os
import json

# CRUD
def account_create(username, password, riotID, region, banned=False):
    account = [username, password, riotID, region, banned]
    accounts.append(account)

def accounts_read():
    global accounts
    print("index\tusername\tpassword\triot id\tregion\t\t\tbanned")
    for index, account in enumerate(accounts):
        print(f"{index}\t{account[0]}\t{account[1]}\t{account[2]}\t{account[3]}\t{account[4]}")

def account_get(account_id):
    global accounts
    account = accounts[account_id]
    paste_to_clipboard(f"{account[0]}, {account[1]}")

def account_update(account_id, username="", password="", riotid="", region="", banned=False):
    global accounts
    account_edit = accounts[account_id]
    
    if username != "":
        account_edit[0] = username
    if password != "":
        account_edit[1] = password
    if riotid != "":
        account_edit[2] = riotid
    if region != "":
        account_edit[3]
    if banned != account_edit[4]:
        account_edit[4] = banned
    
    accounts[account_id] = account_edit

def account_delete(account_id):
    global accounts
    del accounts[account_id]

# DB actions
def save_db():
    dump = json.dumps(accounts, indent=4)
    f = open(FILE, "w")
    f.write(dump)
    f.close

def load_db():
    f = open(FILE, "r")
    undump = json.load(f)
    global accounts
    accounts = undump
    f.close()

# Misc
FILE = "db.json"

def paste_to_clipboard(credentials):
    command = "echo | set /p null=" + credentials.strip() + "| clip"
    os.system(command)

#account list structure: username, password, riotID, banned status
accounts = []

load_db()

while True:
    print("1. create account\n2. read all accounts\n3. get account\n4. update account\n5. delete account\nuse 0 to exit")
    option = input()
    if option == "0":
        save_db()
        break
    
    elif option == "1":
        username = input("insert username: ")
        password = input("insert password: ")
        riot_id = input("insert riot id: ")
        region = input("insert region: ")
        banned = input("is it banned? (y/n): ")
        if banned == "y":
            banned = True
        else:
            banned = False
        account_create(username, password, riot_id, region, banned)

    elif option == "2":
        accounts_read()
    
    elif option == "3":
        account_id = input("insert account id: ")
        account_id = int(account_id)
        account_get(account_id)
    
    elif option == "4":
        print("lazy")
    
    elif option == "5":
        account_id = input("insert account id: ")
        account_id = int(account_id)
        account_delete(account_id)
    
    else:
        print("not in range")