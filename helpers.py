from art import *
from cryptography.fernet import Fernet


def welcome_message():
    print()
    print("--------------------------------------------   Welcome to   --------------------------------------------")
    tprint("Password   Manager")
    print("--------------------------------------------  Version 1.0.1  --------------------------------------------")


def show_instructions():
    print()
    print("""Password Manager is a simple password managing software developed by Arif Faisal (arif.iba34@gmail.com). 
          \nThis program has the following features that you can use:
- Generates random password that can be used across different devices/ platforms/ accounts etc.
- Prompts for login, allowing only you to use the software for your individual needs.
- Stores your password in a secure way.
- Stores multiple passwords for different platforms.
- Let you view your records, including passwords.
- Provides you with a secure key for encryption. You must remember the key, and it should not be shared with anyone. Without the key, the passwords may not be retrieved.
\n----------------------------------------------------------------------------------------------------------""")


def get_user_key():
    print("If you already have a key, type 'N' or 'No' to continue.")
    print("(Keys are required to securely store your password. If you don't have one, type 'Y' or 'Yes)")
    user_key_req = input("Do you need a key? ").lower()

    while True:
        if user_key_req == "y" or user_key_req == "yes":
            # Generate a random key
            user_key = generate_key()
            break
        elif user_key_req == "n" or user_key_req == "no":
            user_key = input("Type your key here: ").encode()
            break
        else:
            print("Invalid input!")

    return user_key


def show_features():
    print()
    print("-----------------------------------------------------------------------------------------------------------")
    tprint("                                 Features")
    print("-----------------------------------------------------------------------------------------------------------")
    print("Type the relevant number from the following to use the feature (i.e.- Enter 1 to generate a random password)")
    print("""
    1 - Generate a Random Password
    2 - Store my Password
    3 - View my Records
    4 - Delete Records
    5 - Generate Key
    6 - Help / FAQ
    7 - Exit
    """)
    relevant_num = input("Enter a number: ")
    return relevant_num


def generate_key():
    user_key = Fernet.generate_key()
    print()
    print("----------------------------------------------------------------------------------------------------------")
    tprint("                           Secure   Key")
    print("----------------------------------------------------------------------------------------------------------")
    print(f"Your key is {user_key.decode()}")
    print("Please remember your key, and store it safely.")
    print("Use the same key for storing, and retrieving your passwords. Otherwise, you may get unexpected results.")
    print("----------------------------------------------------------------------------------------------------------")
    input("Enter any key to continue. ")
    return user_key


def exit_message():
    tprint("Thank   you")
    print("--------------- for using Password Manager! ---------------")
