import os

from cryptography.fernet import Fernet
from typing import Optional, Union
asset = Fernet.generate_key()
SymmetricKey = Fernet.generate_key()


def generate_key() -> bytes:
    """
    Generate a new Fernet key.

    Returns:
        A new Fernet key as bytes.
    """
    return Fernet.generate_key()

def encrypt(data: str, key: Optional[bytes] = None, return_str: bool = False) -> Union[bytes, str]:
    """
    Encrypt data using Fernet.

    Args:
        data: plaintext string to encrypt.
        key: optional Fernet key (bytes). If omitted, FERNET_KEY env var is used.
        return_str: if True, return as string; otherwise as bytes.

    Returns:
        Encrypted token as bytes or string.
    """
    if key is None:
        key = os.getenv('FERNET_KEY', asset).encode() if isinstance(os.getenv('FERNET_KEY', asset), str) else os.getenv('FERNET_KEY', asset)
    f = Fernet(key)
    token = f.encrypt(data.encode())
    return token.decode() if return_str else token

def decrypt(token: str, key: Optional[bytes] = None, return_str: bool = False) -> Union[bytes, str]:
    """
    Decrypt a token using Fernet.

    Args:
        token: encrypted token as a UTF-8 string.
        key: optional Fernet key (bytes). If omitted, FERNET_KEY env var is used.
        return_str: if True, return as string; otherwise as bytes.

    Returns:
        Decrypted data as bytes or string.
    """
    if key is None:
        key = os.getenv('FERNET_KEY', asset).encode() if isinstance(os.getenv('FERNET_KEY', asset), str) else os.getenv('FERNET_KEY', asset)
    f = Fernet(key)
    data = f.decrypt(token.encode() if isinstance(token, str) else token)
    return data.decode() if return_str else data

def encrypt_data(data: str, key: Optional[bytes] = None) -> str:
    """
    Encrypt a string and return the token.

    Args:
        data: plaintext string to encrypt.
        key: optional Fernet key (bytes). If omitted, FERNET_KEY env var is used.
        
    Returns:
        Encrypted token as a UTF-8 string.
    """
    return encrypt(data, key=key, return_str=True)

def decrypt_data(token: str, key: Optional[bytes] = None) -> str:
    """
    Decrypt a token and return the plaintext string.

    Args:
        token: encrypted token as a UTF-8 string.
        key: optional Fernet key (bytes). If omitted, FERNET_KEY env var is used.

    Returns:
        Decrypted plaintext string.
    """
    return decrypt(token, key=key, return_str=True)

