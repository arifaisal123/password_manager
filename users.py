import sqlite3
import hashlib
from art import *
import pwinput


def register_user(username, email, password):
    """
	Registers user in the database.
	:return: None
	:rtype: Nonetype
    """   
    # Connects with the database
    conn = sqlite3.connect("users.sqlite")
    cur = conn.cursor()              

    # Hashes the password
    password = str(password).encode("UTF-8")
    hash_object = hashlib.sha256(password)
    hex_dig = hash_object.hexdigest()

    # Registers users in the database
    cur.executescript("""
    CREATE TABLE IF NOT EXISTS Users (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        username    TEXT UNIQUE,
        email       TEXT,
        password    TEXT 
    );
    """)

    cur.execute("""INSERT INTO Users (username, email, password) 
        VALUES ( ?, ?, ? )""", ( username, email, hex_dig))
    
    conn.commit()

    # Closes the database
    conn.close()

    tprint("Registration  Completed!")


def login_user():
    """
	Logs the user in after necessary input, and check in database.
	:return: None
	:rtype: Nonetype
    """   
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
