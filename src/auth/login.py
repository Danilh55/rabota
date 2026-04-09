def authenticate(username, password):
    """Простая аутентификация"""
    if username == "admin" and password == "secret":
        return True
    return False

def logout():
    print("User logged out")
