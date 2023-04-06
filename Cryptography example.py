from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(b"Go RiverHawks!")
print(cipher_text)
plain_text = cipher_suite.decrypt(cipher_text)
print(plain_text.decode())