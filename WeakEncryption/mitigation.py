import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password

def check_password(stored_hash, password):
    return bcrypt.checkpw(password.encode(), stored_hash)

# Example usage
password = "mysecretpassword"
hashed = hash_password(password)
is_correct = check_password(hashed, password)
print(hashed)
