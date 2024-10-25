# vulnerable_encryption.py
import hashlib

def hash_password(password):
    # Warning: Deprecated and insecure hashing algorithm.
    md5_hash = hashlib.md5(password.encode()).hexdigest()
    return md5_hash

# Simulating password hashing
password = "mysecretpassword"
print(hash_password(password))
