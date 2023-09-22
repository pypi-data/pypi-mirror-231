from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import binascii

class aes128:
    def __init__(self,secretKey):
        self.secretKey = secretKey
    def aes_encrypt_to_hex(self,plaintext):
        # Ensure the key is exactly 16 bytes (128 bits)
        key = self.secretKey.encode('utf-8').ljust(16, b'\x00')
        # Generate a random IV (Initialization Vector)
        iv = get_random_bytes(16)
        # Create an AES cipher object
        cipher = AES.new(key, AES.MODE_CBC, iv)
        # Pad the plaintext to a multiple of 16 bytes (128 bits)
        plaintext = plaintext.encode('utf-8')
        padded_plaintext = plaintext + b'\x00' * (16 - len(plaintext) % 16)
        # Encrypt the padded plaintext
        ciphertext = iv + cipher.encrypt(padded_plaintext)
        # Convert the ciphertext to hexadecimal
        ciphertext_hex = binascii.hexlify(ciphertext).decode('utf-8')
        return ciphertext_hex
    def aes_decrypt_from_hex(self,encrypted_data_hex):
        try:
            # Convert the hexadecimal data back to binary
            ciphertext = binascii.unhexlify(encrypted_data_hex)

            # Extract the IV (first 16 bytes)
            iv = ciphertext[:16]

            # Ensure the key is exactly 16 bytes (128 bits)
            key = self.secretKey.encode('utf-8').ljust(16, b'\x00')

            # Create an AES cipher object
            cipher = AES.new(key, AES.MODE_CBC, iv)

            # Decrypt the ciphertext
            decrypted_data = cipher.decrypt(ciphertext[16:])

            # Remove padding and decode to plaintext
            plaintext = decrypted_data.rstrip(b'\x00').decode('utf-8')

            return plaintext
        except (ValueError, KeyError):
            # If the decryption fails (e.g., due to incorrect password or data), return None
            return None
