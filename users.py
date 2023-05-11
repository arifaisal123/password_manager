import sqlite3
import hashlib
import pwinput
from art import *
import re


def register_user():
    print()
    print("----------------------------------------------------------------------------------------------------------")
    tprint("                  Registration")
    print("----------------------------------------------------------------------------------------------------------")
    
    # Connects with the database
    conn = sqlite3.connect("users.sqlite")
    cur = conn.cursor()

    # Validates username
    while True: 
        username = input("Type your username: ")
        try:
            cur.execute("SELECT username FROM Users WHERE username = ?", (username, ))
            is_duplicate_username = cur.fetchone()[0]
            print(is_duplicate_username)
            if is_duplicate_username:
                print("Username has already been taken. Please try a different one!")
        except:
            if len(username) < 6:
                print("Username should have at least 6 characters.")
            else:    
                break

    # Validates email
    while True:
        email = input("Type your email: ")
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if re.match(pattern, email):
            break
        else:
            print("Please enter a valid email address!")

    # Validates password
    while True:
        password = pwinput.pwinput(prompt="Type your password: ", mask="*")
        if len(password) < 6:
            print("Passwords need to be at least 6 characters long.")
        else:
            break

    # Matches password
    while True:
        confirm_password = pwinput.pwinput(prompt="Confirm your password: ", mask="*")
        if password == confirm_password:
            break
        else:
            print("Passwords don't match! Please type again.")

    # Hashing the password
    password = str(password).encode("UTF-8")
    hash_object = hashlib.sha256(password)
    hex_dig = hash_object.hexdigest()

    # Register users in the database
    
    cur.executescript('''
    CREATE TABLE IF NOT EXISTS Users (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        username    TEXT UNIQUE,
        email       TEXT,
        password    TEXT 
    );
    ''')

    cur.execute("""INSERT INTO Users (username, email, password) 
        VALUES ( ?, ?, ? )""", ( username, email, hex_dig))
    
    conn.commit()

    # Closes the database
    conn.close()

    tprint("Registration  Completed!")


def login_user():
    print()
    print("----------------------------------------------------------------------------------------------------------")
    tprint("                                    Login")
    print("----------------------------------------------------------------------------------------------------------")
    while True:
        conn = sqlite3.connect('users.sqlite')
        cur = conn.cursor()
        
        username = input("Type your username: ")
        password = pwinput.pwinput(prompt="Type your password: ", mask="*")
        hashed_password = hashlib.sha256(password.encode("UTF-8")).hexdigest()

        cur.execute("SELECT * FROM Users WHERE username = ?", (username, ))
        result = cur.fetchone()[1]

        if not result:
            print("Username does not exist!")

        cur.execute("SELECT password FROM Users WHERE username = ?", (username, ))
        result = cur.fetchone()[0]

        if result == hashed_password:
            break
        else:
            print("Incorrect Password!")

    # Closes the database
    conn.close()

    tprint("   Login  Successful!")
    print("----------------------------------------------------------------------------------------------------------")
    return username
