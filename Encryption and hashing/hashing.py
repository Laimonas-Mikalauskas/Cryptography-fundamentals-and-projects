from passlib.hash import passlib_pbkdf2_sha256 as pbkdf2_sha256


def hash_password(password: str) -> str:
    """
    Hashes a password using PBKDF2 with SHA-256.

    Args:
        password (str): The password to hash.

    Returns:
        str: The hashed password.
    """
    return pbkdf2_sha256.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    """
    Verifies a password against a hashed value.

    Args:
        password (str): The password to verify.
        hashed (str): The hashed password to compare against.

    Returns:
        bool: True if the password matches the hash, False otherwise.
    """
    return pbkdf2_sha256.verify(password, hashed)

password = "my_secure_password"
hashed_password = hash_password(password)
print(f"Original password: {password}")
print(f"Hashed password: {hashed_password}")