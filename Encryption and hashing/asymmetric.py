from cryptography.fernet import Fernet
from typing import Optional, Union

AsymmetricKey = Fernet.generate_key()

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
        key = AsymmetricKey
    f = Fernet(key)
    token = f.encrypt(data.encode())
    return token.decode() if return_str else token

def decrypt(data: str, key: Optional[bytes] = None, return_str: bool = False) -> Union[bytes, str]:
    """
    Decrypt a token using Fernet.

    Args:
        data: encrypted token as a UTF-8 string.
        key: optional Fernet key (bytes). If omitted, FERNET_KEY env var is used.
        return_str: if True, return as string; otherwise as bytes.

    Returns:
        Decrypted data as bytes or string.
    """
    if key is None:
        key = AsymmetricKey
    f = Fernet(key)
    decrypted_data = f.decrypt(data.encode() if isinstance(data, str) else data)
    return decrypted_data.decode() if return_str else decrypted_data 