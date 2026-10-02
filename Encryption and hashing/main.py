# Example usage
from cryptography.fernet import Fernet

# Generate a key for encryption/decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# A secret message
message = b"Hello, World!"

# Encrypt the message
cipher_text = cipher_suite.encrypt(message)
print(f"Encrypted: {cipher_text}")

# Decrypt the message
plain_text = cipher_suite.decrypt(cipher_text)
print(f"Decrypted: {plain_text.decode()}")


