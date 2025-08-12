from cryptography.fernet import Fernet
from utils import generate_key

def encrypt_file(filepath: str, password: str):
    key = generate_key(password)
    fernet = Fernet(key)
    
    with open(filepath, 'rb') as file:
        original = file.read()
    
    encrypted = fernet.encrypt(original)
    
    encrypted_path = filepath + ".enc"
    with open(encrypted_path, 'wb') as enc_file:
        enc_file.write(encrypted)
    
    print(f"Encrypted file saved as: {encrypted_path}")

def decrypt_file(filepath: str, password: str):
    key = generate_key(password)
    fernet = Fernet(key)
    
    with open(filepath, 'rb') as enc_file:
        encrypted = enc_file.read()
    
    try:
        decrypted = fernet.decrypt(encrypted)
    except Exception:
        print("❌ Wrong password or corrupted file!")
        return
    
    if filepath.endswith(".enc"):
        output_path = filepath[:-4] + ".dec"
    else:
        output_path = filepath + ".dec"
    
    with open(output_path, 'wb') as dec_file:
        dec_file.write(decrypted)
    
    print(f"Decrypted file saved as: {output_path}")
