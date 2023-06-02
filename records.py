import sqlite3
from art import *
from tabulate import tabulate
from cryptography.fernet import Fernet
import pwinput


def store_records(owner, fernet):
    """
	Stores records of the user (owner, website, username, password) in the database.
	:return: None
	:rtype: Nonetype
    """   
    # Stores passwords in the database
    conn = sqlite3.connect('records.sqlite')
    cur = conn.cursor()
    
    cur.executescript("""
    CREATE TABLE IF NOT EXISTS Records (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        owner       TEXT,
        website     TEXT, 
        username    TEXT,
        password    TEXT
    );
    """)

    while True:
        # Takes user input for records
        website = input("Enter website name: ")
        username = input("Enter username: ")
        password = pwinput.pwinput(prompt="Enter password: ", mask="*")

        # Encrypts a password
        password = password.encode()
        encrypted_password = fernet.encrypt(password)

        cur.execute('''INSERT INTO Records (owner, website, username, password) 
            VALUES ( ?, ?, ?, ? )''', ( owner, website, username, encrypted_password))
        
        conn.commit()

        print("-----------------------------------------------------------------------------------------------------------")
        tprint("                            Success!")
        print("                                     Records have been updated!")
        print("----------------------------------------------------1-------------------------------------------------------")

        user_input = input("Do you want to insert another record? (Yes/No) ").lower()
        if user_input == "no" or user_input == "n":
            break

    # Closes the database
    conn.close()

 
def show_records(user, fernet):
    """
	Shows all the records of the user from the database.
	:return: None
	:rtype: Nonetype
    """   
    # Decrypt the password
    conn = sqlite3.connect('records.sqlite')
    cur = conn.cursor()
    try:
        cur.execute("SELECT EXISTS(SELECT 1 FROM Records WHERE owner = ?)", (user, ))
        is_record_available = cur.fetchone()[0]
        if is_record_available:
            print()
            print("-----------------------------------------------------------------------------------------------------------")
            tprint("                                 Warning!")
            print("-----------------------------------------------------------------------------------------------------------")
            user_input = input("Your passwords will be decrypted, and shown to you on the screen. Are you sure to continue? (Yes/No) ").lower()
            if user_input == "yes" or user_input == "y":                
                cur.execute("SELECT * FROM Records WHERE owner = ?", ( user, ))
                results = cur.fetchall()
                decrypted_records = []
                for result in results:
                    decrypted_record = list(result)
                    decrypted_record[4] = fernet.decrypt(result[4]).decode()
                    decrypted_records.append(decrypted_record)   
                headers = ["ID", "Owner", "Website", "Username", "Password"]
                print(tabulate(decrypted_records, headers=headers, tablefmt="psql"))
        else:
            print()
            print("----------------------------------------------------------------------------------------------------------")
            tprint("                         No   Records!")
            print("----------------------------------------------------------------------------------------------------------")
            print("There are no records available.") 
    except:
        print()
        print("----------------------------------------------------------------------------------------------------------")
        tprint("                         No   Records!")
        print("----------------------------------------------------------------------------------------------------------")
        print("There are no records available.") 
    finally:
        # Closes the database
        conn.close()
    

def delete_records(user):
    """
	Deletes records of the user from the database.
	:return: None
	:rtype: Nonetype
    """   
    conn = sqlite3.connect('records.sqlite')
    cur = conn.cursor()
    
    user_input = input("Do you want to delete all records or some selected ones? (Press 1 for all, 2 for selected ones) ")
    if user_input == "1":
        print("-----------------------------------------------------------------------------------------------------------")
        tprint("                             Warning!")
        print("-----------------------------------------------------------------------------------------------------------")
        reprompt = input("Are you sure you want to delete all records? This operation cannot be reversed! (Type 'Yes' or 'No') ").lower()
        if reprompt == "yes":
            cur.execute("DELETE FROM Records WHERE owner = ?", ( user, ))
            print("-----------------------------------------------------------------------------------------------------------")
            tprint("                            Success!")
            print("                                     Records have been deleted!")
            print("-----------------------------------------------------------------------------------------------------------")
    elif user_input == "2":
        while True:
            record_id = input("Enter the ID of the record that you want to delete: ")
            cur.execute("DELETE FROM Records WHERE owner = ? AND id = ?", ( user, record_id))
            print("-----------------------------------------------------------------------------------------------------------")
            tprint("                            Success!")
            print("                                     Records have been updated!")
            print("-----------------------------------------------------------------------------------------------------------")
            user_input = input("Do you want to delete any more records? (Type 'Yes' or 'No') ").lower()
            if user_input == "no":
                break
    
    conn.commit()
    conn.close()
