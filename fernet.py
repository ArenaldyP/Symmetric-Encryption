from cryptography.fernet import Fernet

key = Fernet.generate_key()
# print(key)
fernet = Fernet(key)
# print(fernet)

# MENGENKRIPSI FILE DAN MENAMBAH DENGAN HASH
token = fernet.encrypt(b"plaintext")

# MENGDEKRIPSI FILE
decrypt = fernet.decrypt(token)
print(decrypt)