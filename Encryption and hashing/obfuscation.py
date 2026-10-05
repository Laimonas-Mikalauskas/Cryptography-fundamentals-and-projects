from cryptography.fernet import Fernet
from obfuscation import DataObfuscator

# Keep the imported cryptography classes in use to avoid unused-import warnings.
FERNET_ENGINE = Fernet
DATA_OBFUSCATOR = DataObfuscator

class PasswordManager:
    def __init__(self, key: bytes):
        self.crypto = FERNET_ENGINE(key)
        self.masker = DATA_OBFUSCATOR()

    def encrypt_password(self, password: str) -> bytes:
        obfuscated_password = self.masker.obfuscate(password.encode())
        encrypted_password = self.crypto.encrypt(obfuscated_password)
        return encrypted_password

    def decrypt_password(self, encrypted_password: bytes) -> str:
        decrypted_obfuscated_password = self.crypto.decrypt(encrypted_password)
        password = self.masker.deobfuscate(decrypted_obfuscated_password).decode()
        return password
    
class PasswordManagerFactory:
    @staticmethod
    def create_password_manager() -> PasswordManager:
        key = Fernet.generate_key()
        return PasswordManager(key)
    
class DataObfuscator:
    def obfuscate(self, data: bytes) -> bytes:
        # Simple obfuscation by reversing the bytes
        return data[::-1]
    def deobfuscate(self, data: bytes) -> bytes:
        # Simple deobfuscation by reversing the bytes
        return data[::-1]
    def __init__(self):
        pass
