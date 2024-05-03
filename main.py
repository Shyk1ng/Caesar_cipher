class CaesarCipher:
    def __init__(self, rotation: int) -> None:
        self.rotation = rotation

    def encrypt_string(self, plaintext: str) -> str:
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                shifted_char = chr(((ord(char.lower()) - ord('a') + self.rotation) % 26) + ord('a'))
                if char.isupper():
                    shifted_char = shifted_char.upper()
                ciphertext += shifted_char
            else:
                ciphertext += char
        return ciphertext

    def decrypt_string(self, ciphertext: str) -> str:
        return self.encrypt_string(ciphertext)


if __name__ == "__main__":
    rotation = int(input("Enter rotation value: "))
    cipher = CaesarCipher(rotation)

    plaintext = input("Enter string to encrypt: ")
    encrypted_text = cipher.encrypt_string(plaintext)
    print("Encrypted:", encrypted_text)

    decrypted_text = cipher.decrypt_string(encrypted_text)
    print("Decrypted:", decrypted_text)