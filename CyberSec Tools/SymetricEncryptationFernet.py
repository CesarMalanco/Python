# Author: reDragonCoder

# NOTE: Fernet uses symmetric encryptations, meaning the same key is used
# for both encryptation and decryptation

# NOTE: The generated key is crucial for securoty. It shpuld be kept secret
# and never shared

from cryptography.fernet import Fernet

# Generates a random 32-byte key
key=Fernet.generate_key()

# (Optional) Shows the generated key
print(key)
print('\n')

# Creates a Fernet cipher object using the key
cipher_suite=Fernet(key)

# Encrypt a message (b indicates a byte string which is neccesary for cryptographic operations)
message=b"Hello, this is a secret message."

# Encrypts the message and stores the result (is returned as a byte string)
cipher_text=cipher_suite.encrypt(message)
print(f"Encrypted: {cipher_text}")
print('\n')

# Decrypt the message
plain_text=cipher_suite.decrypt(cipher_text)

# Decodes the decrypted byte into human-readable string
print(f"Decrypted: {plain_text.decode()}")