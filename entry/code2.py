import hashlib # used for encrption
import getpass #

password_manager = {} # store user details

def create_account():
    username = input("Enter your desired username: ")
    password = getpass.getpass("Enter your desired password: ") # getpass library will hide the password from the user
    hashed_password = hashlib.sha256(password.encode()).hexdigest() # hashlib library will hash the password using the sha256 algorithm 
    password_manager[username] = hashed_password
    print("Account created successfully!")

def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest() # decrypt the hashed password 
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("login successful!")
    else:
        print("Invalid password or username!")

def main():
    while True:
        choice = input("[create|login|quit] Enter: ")
        if choice == "create":
            create_account()
        elif choice == "login":
            login()
        elif choice == "quit":
            break
        else: 
            print("Invalid input.")

if __name__ == "__main__": #python idiom
    main()