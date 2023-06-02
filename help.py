from art import *


def get_help():
    """
	Prints all the help commands that are available.
	:return: None
	:rtype: Nonetype
    """
    print("-----------------------------------------------------------------------------------------------------------")
    tprint("                            Help / FAQ")
    print("-----------------------------------------------------------------------------------------------------------")
    print()
    print("1 - What is this software about?")
    print("2 - What are the benefits of using Password Manager, and why should I use one?")
    print("3 - What is a random password?")
    print("4 - How will my password be stored?")
    print("5 - Will my passwords be shown to me in a secure manner?")
    print("6 - Can I delete my records?")
    print("7 - What is a secure key?")
    print("8 - How can I generate a secure key?")
    print("9 - What if there are bugs in software?")
    print("10 - What if the program becomes unresponsive?")
    print("11 - Can multiple people use this software?")
    print("12 - What makes this software really secure?")
    print("13 - Why do I need to provide my email address?")
    print("14 - What is a valid email address?")
    print("15 - I did not receive any email. What do I do?")
    print()
    user_input = input("Enter a number from above to get more information: ")
    help_logic(user_input)


def help_logic(num):
    """
	Generates the right help message, based on user input.
	:return: None
	:rtype: Nonetype
    """
    if num == "1":
        print_help_1()
    elif num == "2":
        print_help_2()
    elif num == "3":
        print_help_3()
    elif num == "4":
        print_help_4()
    elif num == "5":
        print_help_5()
    elif num == "6":
        print_help_6()
    elif num == "7":
        print_help_7()
    elif num == "8":
        print_help_8()
    elif num == "9":
        print_help_9()
    elif num == "10":
        print_help_10()
    elif num == "11":
        print_help_11()
    elif num == "12":
        print_help_12()
    elif num == "13":
        print_help_13()
    elif num == "14":
        print_help_14()
    elif num == "15":
        print_help_15()


def print_help_1():
    """
	Generates relevant help message.
	:return: None
	:rtype: Nonetype
    """
    print("""
    -----------------------------------------------------------------------------------------------------------------------------------------------
                                                            What is this software about?
    The software is a password manager that helps you to manage your passwords better. You are able to generate new passwords that you can use, and 
     store records with name and passwords of different websites, with your own secured key. This makes your password safe, as you are the only one 
       who has the key to decrypt the passwords. Furthermore, the software stores the database in your local storage, making it even more secure. 
    -----------------------------------------------------------------------------------------------------------------------------------------------
    """)


def print_help_2():
    """
	Generates relevant help message.
	:return: None
	:rtype: Nonetype
    """
    print("""
    -----------------------------------------------------------------------------------------------------------------------------------------------
                                      What are the benefits of using Password Manager, and why should I use one?
     We are living in the digital age, where we require to have passwords for every platform that we use online. It often gets trickier for us to
       select the right password, and also remember it. To prevent hackers from having unauthorized access to any of your accounts, it is often 
      preferred to have different passwords for different platforms. However, it often gets difficult to remember them all. Therefore, a password
    manager is quite handy under such circumstances. Password Manager not only manages your records, but also securely stores them. Therefore, only
                                           you have the access to the information with your own unique key. 
    -----------------------------------------------------------------------------------------------------------------------------------------------
    """)


def print_help_3():
    """
	Generates relevant help message.
	:return: None
	:rtype: Nonetype
    """
    print("""
    -----------------------------------------------------------------------------------------------------------------------------------------------
                                                         What is a random password?
     We often need to have passwords for our different platforms. It gets less secure when we use the same passwords in all platforms. On the other
       hand, we also need to ensure that the password that we are using is difficult to predict. For instance- a password like 123456 can easily be 
      compromised. Therefore, a mixture of uppercase, lowercase letters, numbers, punctuations, and special characters can make the passwords strong
       enough that will be difficult to predict. The random password generator feature of this software does exactly that for you. You just need to
           generate the password, copy it, and save it somewhere safe. You can also use the store password feature of this software to save it.
    -----------------------------------------------------------------------------------------------------------------------------------------------
    """)


def print_help_4():
    """
	Generates relevant help message.
	:return: None
	:rtype: Nonetype
    """
    print("""
    -----------------------------------------------------------------------------------------------------------------------------------------------
                                                        How will my password be stored?
     Your password will be fully encrypted, while stored. You will be provided with a key, and only you can decrypt the password, and view it. We
       advice you to securely store your key, as you will be unable to retrieve your records, if you lose your key, or if you enter an incorrect 
          key. Furthermore, we also advice to use only one key per user ID, as it helps you to easily track, and view your records properly.
    -----------------------------------------------------------------------------------------------------------------------------------------------
    """)


def print_help_5():
    """
	Generates relevant help message.
	:return: None
	:rtype: Nonetype
    """
    print("""
    -----------------------------------------------------------------------------------------------------------------------------------------------
                                                Will my passwords be shown to me in a secure manner?
     Absolutely. First of all, this Password Manager stores the information in your local computer. That means only you have access to the database.
      Furthermore, you need to log in first to use this software. This creates another layer of security. Finally, the passwords are not stored in 
     absolute value, rather in an encrypted format. That means, only you (with the use of the key) will be able to decrypt it. Even, before showing
                                 you the passwords, we will prompt you again before displaying it on the screen.
    -----------------------------------------------------------------------------------------------------------------------------------------------
    """)


def print_help_6():
    """
	Generates relevant help message.
	:return: None
	:rtype: Nonetype
    """
    print("""
    -----------------------------------------------------------------------------------------------------------------------------------------------
                                                           Can I delete my records?
     Yes, you can delete all of your records at once, or one by one by providing the unique ID of the record. Please remember that, this operation
                                    is irreversible, and you cannot get back your record, once deleted. 
    -----------------------------------------------------------------------------------------------------------------------------------------------
    """)


def print_help_7():
    """
	Generates relevant help message.
	:return: None
	:rtype: Nonetype
    """
    print("""
    -----------------------------------------------------------------------------------------------------------------------------------------------
                                                             What is a secure key?
      Passwords are stored using encryption method so that it remains safe from unintended intruders. You are provided a secure key, and only with
        this key, you will able to decrypt and retrieve your password. Therefore, we recommend you to store your keys somewhere completely safe.
    -----------------------------------------------------------------------------------------------------------------------------------------------
    """)


def print_help_8():
    """
	Generates relevant help message.
	:return: None
	:rtype: Nonetype
    """
    print("""
    -----------------------------------------------------------------------------------------------------------------------------------------------
                                                        How can I generate a secure key?
       Generating secure key is fairly easy. If you are storing the record for the first time, you will be automatically prompted for key, which 
            you can store. If you want to generate a completely new key, at some point, you can use the 'Generate a secure key' feature.
    -----------------------------------------------------------------------------------------------------------------------------------------------
    """)


def print_help_9():
    """
	Generates relevant help message.
	:return: None
	:rtype: Nonetype
    """
    print("""
    -----------------------------------------------------------------------------------------------------------------------------------------------
                                                       What if there are bugs in software?
     The software is thoroughly tested for bugs. Nonetheless, even after so, If you encounter any bugs while using the software, please report it 
                   at arif.iba34@gmail.com. Please include as much information as possible, with screenshots of the bug occuring. 
    -----------------------------------------------------------------------------------------------------------------------------------------------
    """)


def print_help_10():
    """
	Generates relevant help message.
	:return: None
	:rtype: Nonetype
    """
    print("""
    -----------------------------------------------------------------------------------------------------------------------------------------------
                                                    What if the program becomes unresponsive?
                     If at some point, the program does not respond at all, press CTRL + C from your keyboard to terminate the program.
    -----------------------------------------------------------------------------------------------------------------------------------------------
    """)


def print_help_11():
    """
	Generates relevant help message.
	:return: None
	:rtype: Nonetype
    """
    print("""
    -----------------------------------------------------------------------------------------------------------------------------------------------
                                                     Can multiple people use this software?
      Yes, multiple people can use this software by providing the information at registration. Then, the respective user can log in by providing
                                                                  appropriate details.
    -----------------------------------------------------------------------------------------------------------------------------------------------
    """)


def print_help_12():
    """
	Generates relevant help message.
	:return: None
	:rtype: Nonetype
    """
    print("""
    -----------------------------------------------------------------------------------------------------------------------------------------------
                                                     What makes this software really secure?
      This software takes further steps to ensure that you can store your passwords for different platforms in a secure manner. Firstly, you have
     to register with a password, so that makes your records accessible to you only. The password is hashed, and therefore, there is absolutely no
     chance to get it from the database as well. Secondly, once you start storing your records, your passwords will be encrypted based on a secure
      key (only available to you). You will use the same key to decrypt your password. Even you will get a prompt before the password is displayed
                         on your computer screen. These multi layers of security make the Password Manager secure for your use.
    -----------------------------------------------------------------------------------------------------------------------------------------------
    """)


def print_help_13():
    """
	Generates relevant help message.
	:return: None
	:rtype: Nonetype
    """
    print("""
    -----------------------------------------------------------------------------------------------------------------------------------------------
                                                     Why do I need to provide my email address?
      You will be required to provide your email address during the registration process. Your email will only be used when you prompt for "Forgot
         Password" option. Doing so, you will be provided with an OTP or One Time Password that you need to enter during the process. Currently, 
                                        this feature is in development, and will be available in future release.
    -----------------------------------------------------------------------------------------------------------------------------------------------
    """)


def print_help_14():
    """
	Generates relevant help message.
	:return: None
	:rtype: Nonetype
    """
    print("""
    -----------------------------------------------------------------------------------------------------------------------------------------------
                                                          What is a valid email address?
       A valid email address can have a combination of letters, digits, dots, underscores, percentage signs, and plus and minus signs before the 
      "@" symbol. After the "@" symbol, the email can have a combination of letters, digits, dots, and hyphens before the domain extension (such
                            as ".com" or ".org). Finally, the email will require at least two letters for the domain extension.
    -----------------------------------------------------------------------------------------------------------------------------------------------
    """)


def print_help_15():
    """
	Generates relevant help message.
	:return: None
	:rtype: Nonetype
    """
    print("""
    -----------------------------------------------------------------------------------------------------------------------------------------------
                                                        I did not receive any email. What do I do?
         Please check your spam folder. Additionally, check if your internet connection is working or not at the time of the password request. 
                                  Currently, this feature is in development, and will be available in future release.
    -----------------------------------------------------------------------------------------------------------------------------------------------
    """)
    