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


def main():
    welcome_message()
    show_instructions()
    
    while True:
        print("""Please enter a number from the following: 
        
        1 -- Registration
        2 -- Login
        3 -- Forgot Password
        4 -- Change Password
        """)
        user_input = input("New User? Type 1 to Register, or 2 for Login (Returning User): ")
        if user_input == "1":
            register_user()
            current_user = login_user()
            break
        elif user_input == "2":
            current_user = login_user()
            break
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            print("Invalid input!")
    
    user_key = get_user_key()
    
    # Create a Fernet object with the key
    fernet = Fernet(user_key)

    while True:
        feature_num = show_features()
        program_logic(feature_num, current_user, fernet)


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


if __name__ == "__main__":
    main()
