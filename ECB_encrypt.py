from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from Crypto.Cipher import AES
import os

# Kunci harus berukuran 128, 192, atau 256 bits
kunci_aes = os.urandom(32)  # Menghasilkan kunci acak dengan ukuran 256 bits

# Membuat objek sandi dengan algoritma AES dalam mode ECB
sandi_hazmat = Cipher(
    algorithms.AES(kunci_aes),
    modes.ECB(),
    backend=default_backend()
)

# Membuat enkriptor untuk melakukan enkripsi
enkriptor_hazmat = sandi_hazmat.encryptor()

# Contoh plaintext dengan ukuran blok 128-bit (16 bytes)
plaintext = b"block size = 128"

# Memastikan panjang plaintext adalah kelipatan dari panjang blok
panjang_plaintext = len(plaintext)
if panjang_plaintext % 16 != 0:
    # Jika tidak, tambahkan padding (contoh: PKCS7 padding)
    padding_length = 16 - (panjang_plaintext % 16)
    plaintext += bytes([padding_length] * padding_length)

# Melakukan enkripsi terhadap plaintext menggunakan hazmat
a_hazmat = enkriptor_hazmat.update(plaintext) + enkriptor_hazmat.finalize()

# Membuat objek sandi AES baru dengan kunci acak
kunci_pycrypto = os.urandom(32)  # Menghasilkan kunci acak dengan ukuran 256 bits
sandi_pycrypto = AES.new(kunci_pycrypto, AES.MODE_ECB)

# Melakukan enkripsi terhadap pesan menggunakan kunci acak
# Pastikan panjang pesan adalah kelipatan dari panjang blok
pesan_pycrypto = sandi_pycrypto.encrypt(plaintext)

# Menampilkan pesan terenkripsi dalam bentuk string
print("Pesan terenkripsi (hazmat):", a_hazmat.hex())
print("Pesan terenkripsi (pycrypto):", pesan_pycrypto.hex())
