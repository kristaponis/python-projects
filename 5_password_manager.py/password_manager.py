from cryptography.fernet import Fernet

# def pass_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)

# pass_key()

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open("passwords.txt", "r") as pwd:
        for line in pwd.readlines():
            data = line.strip()
            user, passw = data.split("|")
            print(f"User name: {user}, Password: {fer.decrypt(passw.encode()).decode()}")

def add():
    name = input("Account name: ")
    password = input("Password: ")
    with open("passwords.txt", "a") as pwd:
        pwd.write(f"{name}|{fer.encrypt(password.encode()).decode()}\n")



while True:
    print("Would you like to add password?")
    print("Would you like to view passwords?")
    print("Enter 'q' for quit program")
    print("Enter 'add' to add password")
    print("Enter 'view' to view passwords")
    action = input()
    if action == "q":
        break
    elif action == "add":
        add()
    elif action == "view":
        view()
    else:
        print("Enter 'q', 'add' or 'view'")
        continue

