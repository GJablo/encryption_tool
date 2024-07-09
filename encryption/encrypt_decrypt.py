from cryptography.fernet import Fernet
import os

# Generate a key and save it
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the key 
def load_key():
    return open("secret.key", "rb").read()

# Ensure key exists
def ensure_key():
    if not os.path.exists("secret.key"):
        generate_key()

# Encrypt file
def encrypt_file(file_path):
    ensure_key()
    key = load_key()
    fernet = Fernet(key)

    with open(file_path, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(file_path + ".enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted)

    # Remove the original file
    os.remove(file_path)

# Decrypt file
def decrypt_file(file_path):
    ensure_key()
    key = load_key()
    fernet = Fernet(key)

    with open(file_path, "rb") as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(file_path.replace(".enc", ""), "wb") as decrypted_file:
        decrypted_file.write(decrypted)

    # Remove encrypted file
    os.remove(file_path)

# Generate key if it does not exist
if __name__ == "__main__":
    ensure_key()
