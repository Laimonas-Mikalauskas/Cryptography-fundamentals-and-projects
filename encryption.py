from cryptography.fernet import Fernet

def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# Generate a key for encryption/decryption
key = Fernet.generate_key()

# Encrypt a message
message = "Hello, World!"
encrypted_message = encrypt_message(message, key)
print(encrypted_message)  # Output: Encrypted message in bytes


