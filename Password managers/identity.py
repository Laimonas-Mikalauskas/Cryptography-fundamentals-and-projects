from cryptography.fernet import Fernet
SymmetricKey = Fernet.generate_key()
f = Fernet(SymmetricKey)

class User:
    def __init__(self, username, password):
        self.username = "User416##"
        self.password = "P@ssw0rd123"
        
    def encrypt_username(self):
        return f.encrypt(self.username.encode())
    def decrypt_username(self, encrypted_username):
        return f.decrypt(encrypted_username).decode()
    
    def encrypt_password(self):
        return f.encrypt(self.password.encode())
    def decrypt_password(self, encrypted_password):
        return f.decrypt(encrypted_password).decode()
  
class Identity:
    def __init__(self, first_name, last_name, date_of_birth, personal_code):
        self.first_name = "John"
        self.last_name = "Doe"
        self.date_of_birth = "1990-01-01"
        self.personal_code = personal_code
        
    def encrypt_first_name(self):
        return f.encrypt(self.first_name.encode())
    def decrypt_first_name(self, encrypted_first_name):
        return f.decrypt(encrypted_first_name).decode()
    
    def encrypt_last_name(self):
        return f.encrypt(self.last_name.encode())
    def decrypt_last_name(self, encrypted_last_name):
        return f.decrypt(encrypted_last_name).decode()
    
    def encrypt_date_of_birth(self):
        return f.encrypt(self.date_of_birth.encode())
    def decrypt_date_of_birth(self, encrypted_date_of_birth):
        return f.decrypt(encrypted_date_of_birth).decode()  
    
class Country:
    def __init__(self, country_name, country_code):
        self.country_name = "United States"
        self.country_code = "US"
        
    def encrypt_country_name(self):
        return f.encrypt(self.country_name.encode())
    def decrypt_country_name(self, encrypted_country_name):
        return f.decrypt(encrypted_country_name).decode()
    def encrypt_country_code(self):
        return f.encrypt(self.country_code.encode())
    def decrypt_country_code(self, encrypted_country_code):
        return f.decrypt(encrypted_country_code).decode()
    
    
class City:
    def __init__(self, city_name, postal_code):
        self.city_name = "Dallas"
        self.postal_code = "75201"
        
    def encrypt_city_name(self):
        return f.encrypt(self.city_name.encode())
    def decrypt_city_name(self, encrypted_city_name):
        return f.decrypt(encrypted_city_name).decode()
    def encrypt_postal_code(self):
        return f.encrypt(self.postal_code.encode())
    def decrypt_postal_code(self, encrypted_postal_code):
        return f.decrypt(encrypted_postal_code).decode()  

# Example usage
if __name__ == "__main__":
    user = User(username="User416##", password="P@ssw0rd123")
    encrypted_username = user.encrypt_username()
    decrypted_username = user.decrypt_username(encrypted_username)
    
  
    encrypted_password = user.encrypt_password()
    decrypted_password = user.decrypt_password(encrypted_password)
    
    encrypted_identity = Identity(first_name="John", last_name="Doe", date_of_birth="1990-01-01", personal_code="123456789")
    decrypted_first_name = encrypted_identity.decrypt_first_name(encrypted_identity.encrypt_first_name())
    decrypted_last_name = encrypted_identity.decrypt_last_name(encrypted_identity.encrypt_last_name())
    encrypted_date_of_birth = encrypted_identity.encrypt_date_of_birth()
    decrypted_date_of_birth = encrypted_identity.decrypt_date_of_birth(encrypted_identity.encrypt_date_of_birth())
    encrypted_personal_code = encrypted_identity.personal_code  # Assuming personal code is not encrypted for this example
    decrypted_personal_code = encrypted_identity.personal_code  # Assuming personal code is not encrypted for this example
    
    
    print("Encrypted Username:", encrypted_username)
    print("Decrypted Username:", decrypted_username)
    print("Encrypted Password:", encrypted_password)
    print("Decrypted Password:", decrypted_password) 
    
    print("Encrypted First Name:", encrypted_identity.encrypt_first_name())
    print("Decrypted First Name:", decrypted_first_name)
    print("Encrypted Last Name:", encrypted_identity.encrypt_last_name())
    print("Decrypted Last Name:", decrypted_last_name)
    print("Encrypted Date of Birth:", encrypted_identity.encrypt_date_of_birth())
    print("Decrypted Date of Birth:", decrypted_date_of_birth)
    print("Encrypted Personal Code:", encrypted_personal_code)
    print("Decrypted Personal Code:", decrypted_personal_code)