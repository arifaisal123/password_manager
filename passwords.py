from password_generator import PasswordGenerator

def generate_password():
    pw = PasswordGenerator()
    generate_pw = pw.generate()
    return generate_pw


def forgot_password():
    otp = generate_password()


def change_password():
    pass

