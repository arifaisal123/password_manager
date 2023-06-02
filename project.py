"""
Developed by Arif Faisal (arif.iba34@gmail.com)
The MIT License (MIT)

Copyright (c) 2023 Arif Faisal

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), 
to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
IN THE SOFTWARE.
"""

from cryptography.fernet import Fernet
from help import *
from users import *
from records import *
from helpers import *
from passwords import *
from art import *
from validation import *
import pwinput


def main():
    # Prints welcome message, and the version of the software
    welcome_message()

    # Prints instructions on how to use the software
    show_instructions()
    
    # Initial login/ registration prompt
    while True:
        print("""Please enter a number from the following: 
        
        1 -- Registration
        2 -- Login
        3 -- Forgot Password
        4 -- Change Password
        """)

        user_input = input("New User? Type 1 to Register, or 2 for Login (Returning User): ")
        if user_input == "1":
            print()
            print("----------------------------------------------------------------------------------------------------------")
            tprint("                  Registration")
            print("----------------------------------------------------------------------------------------------------------")
            
            username, email, password = input_validation()

            register_user(username, email, password)
            current_user = login_user()
            break
        
        elif user_input == "2":
            current_user = login_user()
            break
        
        elif user_input == "3":
            print("------------------------------------------------------------------------------------------------")
            tprint("In   Development")
            print("This feature is currently in development, and will be added in the future release.")
            print("------------------------------------------------------------------------------------------------")
        
        elif user_input == "4":
            print("------------------------------------------------------------------------------------------------")
            tprint("In   Development")
            print("This feature is currently in development, and will be added in the future release.")
            print("------------------------------------------------------------------------------------------------")
        
        else:
            print("Invalid input!")
    
    # Gets unique user key for the user
    user_key = get_user_key()
    
    # Create a Fernet object with the key
    fernet = Fernet(user_key)

    # Prompt the user for feature number to be used
    while True:
        feature_num = show_features()
        program_logic(feature_num, current_user, fernet)


# Takes user input, and generate the right feature
def program_logic(num, user, fernet):
    if num == "1":
        random_pass = generate_password()
        print(f"Your random password is: {random_pass}")
        print()
    elif num == "2":
        store_records(user, fernet)
        print()
    elif num == "3":
        show_records(user, fernet)
        print()
    elif num == "4":
        delete_records(user)
        print()
    elif num == "5":
        generate_key()
        print()
    elif num == "6":
        get_help()
        print()
    elif num == "7":
        exit_message()
        exit()

    user_input = input("Do you want to continue? (Enter any key to view features, or 7 to exit) ")
    
    if user_input == "7":
        exit_message()
        exit()


def input_validation():
    """
	Validates the input provided by the user.
	:return: username, email, and password as stringss
	:rtype: str
    """
    
    # Validates username
    while True:
        username = input("Type your username: ")
        if validate_username(username):
            break

    # Validates email
    while True:
        email = input("Type your email: ")
        if validate_email(email):
            break

    # Validates password
    while True:
        password = pwinput.pwinput(prompt="Type your password: ", mask="*")
        if validate_password(password):
            break
        
    # Matches password
    while True:
        confirm_password = pwinput.pwinput(prompt="Confirm your password: ", mask="*")
        if validate_password_match(password, confirm_password):
            break

    return username, email, password


# When the program runs, the script will function (not available on imports)
if __name__ == "__main__":
    main()
