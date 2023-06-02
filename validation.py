import re

def validate_username(username):
    """
	Validates the username.
	:return: True if validation is successful, otherwise raise ValueError.
	:rtype: Boolean
    """   
    # Username first letter validation
    if not username[0].isalpha():
        raise ValueError("Username must start with alphabets.")
    
    # Username length validation 
    if len(username) < 6 or len(username) > 15:
        raise ValueError("Username should be between 6 to 15 characters inclusive.")
    
    # Checks username for duplication
    while True: 
        try:
            cur.execute("SELECT username FROM Users WHERE username = ?", (username, ))
            is_duplicate_username = cur.fetchone()[0]
            if is_duplicate_username:
                print("Username has already been taken. Please try a different one!")
        except:
            # Since there is no duplication of users, it will break out of loop
            break

    return True    


def validate_email(email):
    """
	Validates the email.
	:return: True if validation is successful, otherwise raise ValueError.
	:rtype: Boolean
    """  
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(pattern, email):
        return True
    else:
        raise ValueError("Please enter a valid email address!")


def validate_password(password):
    """
	Validates the password.
	:return: True if validation is successful, otherwise raise ValueError.
	:rtype: Boolean
    """ 
    if len(password) < 6:
            raise ValueError("Passwords need to be at least 6 characters long.")
    return True


def validate_password_match(password, confirm_password):
    """
	Validates the password match.
	:return: True if validation is successful, otherwise raise ValueError.
	:rtype: Boolean
    """ 
    if password == confirm_password:
        return True
    else:
        raise ValueError("Passwords don't match! Please type again.")
