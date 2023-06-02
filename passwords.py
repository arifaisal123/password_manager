from password_generator import PasswordGenerator

# 
def generate_password():
    """
	Generates a random password.
	:return: Randomly generated string containing uppercase/lowercase letters, numbers, special chars, punctuations.
	:rtype: str
    """
    pw = PasswordGenerator()
    generate_pw = pw.generate()
    print(type(generate_pw))
    return generate_pw

# Generates a new password for safe login, if user forgets password [in development]
def forgot_password():
    pass

# Changes user password [in development]
def change_password():
    pass
