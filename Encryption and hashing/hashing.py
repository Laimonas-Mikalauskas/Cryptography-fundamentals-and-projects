from passlib.hash import sha256_crypt

def hash_password(password: str) -> str:
    return sha256_crypt.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    return sha256_crypt.verify(password, hashed)

def main():
    # Example usage
    password = "my_secure_password"
    hashed_password = hash_password(password)
    print(f"Hashed Password: {hashed_password}")
    print(type(f"Hashed Password: {hashed_password}"))

    # Verify the password
    is_valid = verify_password(password, hashed_password)
    print(f"Password is valid: {is_valid}")
    print(type(f"Password is valid: {is_valid}"))