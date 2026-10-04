# 1. Example usage
from cryptography.fernet import Fernet


# 2. Generate a key for encryption/decryption
# Generated random 32-byte key for Fernet symmetric encryption
# Note: In practice, you should securely store this key by keeping it secret
key = Fernet.generate_key()

# 3. Initialize the Fernet class with the generated key
cipher_suite = Fernet(key)

# 4. Define a secret message
# Messages must be in bytes, so we encode the string to bytes
message = b"Hello, World!"

# 5. Encrypt the message
cipher_text = cipher_suite.encrypt(message)
print(f"Encrypted: (Cipher Text): {cipher_text.decode()}")

# 6. Decrypt the message
plain_text = cipher_suite.decrypt(cipher_text)
print(f"Decrypted: (Plain Text): {plain_text.decode()}")

