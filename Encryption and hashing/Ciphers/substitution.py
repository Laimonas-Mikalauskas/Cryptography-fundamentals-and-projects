import random

def generate_substitution_key():
    
    """
    Generates a random substitution key for a simple substitution cipher.
    
    Returns:
        dict: A dictionary mapping each letter of the alphabet to a randomly chosen letter.
    """
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    shuffled_alphabet = alphabet.copy()
    random.shuffle(shuffled_alphabet)
    
    substitution_key = {original: substituted for original, substituted in zip(alphabet, shuffled_alphabet)}
    
    return substitution_key

def encrypt_substitution(plaintext, substitution_key):
    """
    Encrypts the given plaintext using the provided substitution key.
    
    Args:
        plaintext (str): The text to be encrypted.
        substitution_key (dict): A dictionary mapping each letter of the alphabet to a substituted letter.
    
    Returns:
        str: The encrypted ciphertext.
    """
    ciphertext = ''
    
    for char in plaintext.upper():
        if char in substitution_key:
            ciphertext += substitution_key[char]
        else:
            ciphertext += char  # Non-alphabetic characters are not substituted
    
    return ciphertext

my_substitution_key = generate_substitution_key()
print("Substitution Key:", my_substitution_key)    