import pytest
from project import validate_username, validate_email, validate_password, validate_password_match


# Tests the validate_username function
def test_validate_username():
    with pytest.raises(ValueError):
        validate_username("123testing")
        validate_username("tstb6")
        validate_username("testingvalidationformorethan15characters") 
        validate_username("test_for_16chars")
    assert validate_username("test_for15chars") == True
    assert validate_username("testusername123") == True
    assert validate_username("test12") == True


def test_validate_email():
    with pytest.raises(ValueError):
        validate_email("abc.com")
        validate_email("_@abc.com")
        validate_email("abc@_abc.com")
        validate_email("abc@gmailcom")
        validate_email("abc@gmail@abc.com")
        validate_email("abc@gmail.")
        validate_email("abc@gmail.com.co")
    assert validate_email("name@gmail.com") == True
    assert validate_email("john_woodgate@yahoo.com") == True
    assert validate_email("smith123@hotmail.com") == True
   

def test_validate_password():
    with pytest.raises(ValueError):
        validate_password("test1")
        validate_password("less")
        validate_password("")
    assert validate_password("test_6") == True
    assert validate_password("CheckingTestPassword657") == True
    assert validate_password("d9$for123_ty@98") == True


def test_validate_password_match():
    with pytest.raises(ValueError):
        validate_password_match("testpass", "testpasss")
        validate_password_match("testpasS", "testpass")
    assert validate_password_match("passmanager123", "passmanager123") == True
    assert validate_password_match("TrDt2006", "TrDt2006") == True
