import math

def transposition_encrypt(plaintext, key):
    # Remove spaces from the plaintext
    plaintext = plaintext.replace(" ", "")
    
    # Calculate the number of columns
    num_columns = len(key)
    
    # Calculate the number of rows needed
    num_rows = math.ceil(len(plaintext) / num_columns)
    
    # Create a list to hold the columns
    columns = [''] * num_columns
    
    # Fill the columns with characters from the plaintext
    for i in range(len(plaintext)):
        column_index = i % num_columns
        columns[column_index] += plaintext[i]
    
    # Create the ciphertext by reading the columns in order of the key
    ciphertext = ''
    for index in sorted(range(len(key)), key=lambda k: key[k]):
        ciphertext += columns[index]
    
    return ciphertext

def transposition_decrypt(ciphertext, key):
    # Calculate the number of columns
    num_columns = len(key)
    
    # Calculate the number of rows needed
    num_rows = math.ceil(len(ciphertext) / num_columns)
    
    # Create a list to hold the columns
    columns = [''] * num_columns
    
    # Fill the columns with characters from the ciphertext
    for i in range(len(ciphertext)):
        column_index = sorted(range(len(key)), key=lambda k: key[k])[i % num_columns]
        columns[column_index] += ciphertext[i]
    
    # Create the plaintext by reading the rows
    plaintext = ''
    for row in range(num_rows):
        for col in range(num_columns):
            if row < len(columns[col]):
                plaintext += columns[col][row]
    
    return plaintext

# Example usage
msg = "HELLO WORLD"
key = "3142"
ciphertext = transposition_encrypt(msg, key)

print("Ciphertext:", ciphertext)
plaintext = transposition_decrypt(ciphertext, key)
print("Plaintext:", plaintext)

