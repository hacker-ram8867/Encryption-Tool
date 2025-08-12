import hashlib
import base64
from cryptography.fernet import Fernet

def generate_key(password: str) -> bytes:
    """
    Generate a Fernet key from the password using SHA-256 hashing.
    """
    hash = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(hash)
