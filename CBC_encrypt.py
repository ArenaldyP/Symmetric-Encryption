import secrets
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Kunci harus berukuran 128, 196, atau 256 bit
kunci = secrets.token_bytes(32)

def encrypt(data):
    # Menghasilkan 16 byte acak sebagai IV (Initialization Vector)
    iv = secrets.token_bytes(16)

    # Menggunakan AES dalam mode CBC (Cipher Block Chaining)
    cipher = Cipher(
        algorithms.AES(key=kunci),
        modes.CBC(iv),
        backend=default_backend()
    )
    encryptor = cipher.encryptor()

    # Mengenkripsi data dengan AES-CBC
    ciphertext = encryptor.update(data) + encryptor.finalize()

    # Mengembalikan IV dan ciphertext untuk keperluan dekripsi
    return iv + ciphertext

# Contoh plaintext
plaintext = b"the same message" * 2

# Mengenkripsi plaintext dengan fungsi encrypt
x = encrypt(plaintext)
y = encrypt(plaintext)

# Mengecek apakah ada pola pada ciphertext
print("Pola pada Ciphertext:", x[:16] == x[16:])

# Mengecek apakah hasil enkripsi dari dua plaintext yang identik sama
print("Enkripsi dari plaintext yang identik sama:", x == y)
