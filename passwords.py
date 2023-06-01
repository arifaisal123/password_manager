from password_generator import PasswordGenerator

# Generates a random password
def generate_password():
    pw = PasswordGenerator()
    generate_pw = pw.generate()
    return generate_pw

# Generates a new password for safe login, if user forgets password [in development]
def forgot_password():
    pass

# Changes user password [in development]
def change_password():
    pass
