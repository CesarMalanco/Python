# Author: reDragonCoder

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Generate a key and initialization vector (IV)
key=get_random_bytes(16)
iv=get_random_bytes(16)

# Encrypt a message
cipher=AES.new(key, AES.MODE_CBC, iv)
message=b"Hello, this is a secret message."
cipher_text=cipher.encrypt(pad(message, AES.block_size))
print(f"Encrypted: {cipher_text}")
print('\n')

# Decrypt the message
cipher=AES.new(key, AES.MODE_CBC, iv)
plain_text=unpad(cipher.decrypt(cipher_text), AES.block_size)
print(f"Decrypted: {plain_text.decode()}")