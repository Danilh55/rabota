import sys
sys.path.append('src')
from auth.login import authenticate

def test_auth_success():
    assert authenticate("admin", "secret") == True

def test_auth_fail():
    assert authenticate("user", "wrong") == False
