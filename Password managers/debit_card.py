from cryptography.fernet import Fernet
SymmetricKey = Fernet.generate_key()
f = Fernet(SymmetricKey)

class DebitCard:
    def __init__(self, card_number, expiration_date, cvv):
        self.card_number = "5544 0088 1316 7710"
        self.expiration_date = "12/25"
        self.cvv = "256"
        
    def encrypt_card_number(self):
        return f.encrypt(self.card_number.encode())
    def decrypt_card_number(self, encrypted_card_number):
        return f.decrypt(encrypted_card_number).decode()
    
    def encrypt_expiration_date(self):
        return f.encrypt(self.expiration_date.encode())
    def decrypt_expiration_date(self, encrypted_expiration_date):
        return f.decrypt(encrypted_expiration_date).decode()
    
    def encrypt_cvv(self):
        return f.encrypt(self.cvv.encode())
    def decrypt_cvv(self, encrypted_cvv):
        return f.decrypt(encrypted_cvv).decode()
    
        
    def add_debit_card(self, debit_card):
        self.debit_cards.append(debit_card)
        
    def get_debit_card(self, card_number):
        for debit_card in self.debit_cards:
            if debit_card.card_number == card_number:
                return debit_card
        return None
    
    def remove_debit_card(self, card_number):
        debit_card = self.get_debit_card(card_number)
        if debit_card:
            self.debit_cards.remove(debit_card)
            return True
        return False 
    
if __name__ == "__main__":
    # Example usage
    debit_card = DebitCard(card_number="5544 0088 1316 7710", expiration_date="12/25", cvv="256") 
    
    # Encrypt and decrypt card number
    encrypted_card_number = debit_card.encrypt_card_number()
    decrypted_card_number = debit_card.decrypt_card_number(encrypted_card_number)
    
    # Encrypt and decrypt expiration date
    encrypted_expiration_date = debit_card.encrypt_expiration_date()
    decrypted_expiration_date = debit_card.decrypt_expiration_date(encrypted_expiration_date)
    
    # Encrypt and decrypt CVV
    encrypted_cvv = debit_card.encrypt_cvv()
    decrypted_cvv = debit_card.decrypt_cvv(encrypted_cvv)
    
    # Print results
    print("Encrypted Card Number:", encrypted_card_number)
    print("Decrypted Card Number:", decrypted_card_number)
    print("Encrypted Expiration Date:", encrypted_expiration_date)
    print("Decrypted Expiration Date:", decrypted_expiration_date)
    print("Encrypted CVV:", encrypted_cvv)
    print("Decrypted CVV:", decrypted_cvv)
    
    
         
    
     