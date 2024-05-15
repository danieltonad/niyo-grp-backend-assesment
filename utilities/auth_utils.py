import hashlib

def hash_pwd(pwd: str) -> str:
    hash_object = hashlib.sha256(pwd.encode())
    return hash_object.hexdigest()

def verify_password(hash: str, raw: str) -> bool:
    return hash_pwd(raw) == hash