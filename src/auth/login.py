import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate(username, password):
    """Аутентификация с хешированием"""
    if not username or not password:
        return False
    hashed = hash_password(password)
    return username == "admin" and hashed == hash_password("secret")

def logout():
    """Завершение сессии"""
    print("Session ended")
