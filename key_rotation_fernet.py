from cryptography.fernet import Fernet, MultiFernet

# kunci_lama = b"jhon"
# fernet_lama = Fernet(kunci_lama)
#
# kunci_baru = Fernet.generate_key()
# fernet_baru = Fernet(kunci_baru)
#
# multi_fernet = MultiFernet([fernet_baru, fernet_lama])
# old_tokens = kunci_lama
# new_tokens = [multi_fernet.rotate(t) for t in old_tokens]
#
# print(new_tokens)

# Generate Kunci
kunci1 = Fernet(Fernet.generate_key())
kunci2 = Fernet(Fernet.generate_key())

# Menggunakan multifernet untuk merotasi kunci
F = MultiFernet([kunci1, kunci2])

# Enkripsi dan generate token
token = F.encrypt(b"Nama Saya adalah Jhon Wick")

# Melihat ciphertext (masih bytes)
print(token)

# Melihat dekripsi dari ciphertext ke text (string)
d = F.decrypt(token)

# Melihat plaintext
print(d.decode())

print("Merotasi Kunci")
kunci3 = Fernet(Fernet.generate_key())
F2 = MultiFernet([kunci1, kunci3, kunci2])
rotasi = F2.rotate(token)
d2 = F2.decrypt(rotasi)
print(d2.decode())
