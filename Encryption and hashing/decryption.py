from cryptography.fernet import Fernet

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message


# Generate a key for encryption/decryption
key = Fernet.generate_key()


# Decrypt the message
message = "Hello, World!"
decrypted_message = decrypt_message(message, key)
print(decrypted_message)  # Output: Hello, World!

