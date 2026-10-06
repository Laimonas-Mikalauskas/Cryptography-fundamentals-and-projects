def caesar_cipher(text, shift):
    """
    Encrypts or decrypts a given text using the Caesar cipher technique.

    Parameters:
    text (str): The input text to be encrypted or decrypted.
    shift (int): The number of positions to shift each letter. 
                 Positive for encryption, negative for decryption.

    Returns:
    str: The resulting encrypted or decrypted text.
    """
    result = ""

    for char in text:
        if char.isalpha():
            # Determine the ASCII offset based on uppercase or lowercase
            offset = ord('A') if char.isupper() else ord('a')
            # Perform the shift and wrap around using modulo 26
            shifted_char = chr((ord(char) - offset + shift) % 26 + offset)
            result += shifted_char
        else:
            # Non-alphabetic characters are added unchanged
            result += char

    return result

def encrypt_caesar(plain_text, shift):
    """
    Encrypts the given plain text using the Caesar cipher.

    Parameters:
    plain_text (str): The text to be encrypted.
    shift (int): The number of positions to shift each letter.

    Returns:
    str: The encrypted text.
    """
    return caesar_cipher(plain_text, shift)

def decrypt_caesar(cipher_text, shift):
    """
    Decrypts the given cipher text using the Caesar cipher.

    Parameters:
    cipher_text (str): The text to be decrypted.
    shift (int): The number of positions to shift each letter.

    Returns:
    str: The decrypted text.
    """
    return caesar_cipher(cipher_text, -shift)

message = "Hello, World!"
key = 3

# Encrypt the message
encrypted_message = encrypt_caesar(message, key)

# Decrypt the message
decrypted_message = decrypt_caesar(encrypted_message, key)

# Print the results
print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted Message: {decrypted_message}")