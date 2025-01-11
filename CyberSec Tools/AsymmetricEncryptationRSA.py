# Author: reDragonCoder

# NOTE: PKCS1_OAEP implements that padding scheme for secure RSA encryptation

# NOTE: RSA.generate(2048) generates a new RSA key pair with a key size of 
# 2048 bits (common for security)

# NOTE: key.export_key() exports the provate key in a format suitable for 
# storage or transmission

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

# Generate RSA keys
key=RSA.generate(2048)
private_key=key.export_key()
public_key=key.publickey().export_key()

# (Optional) Showing private and public key
print(f"Private key: {private_key}")
print('\n')
print(f"Public key: {public_key}")
print('\n')

# Encrypt a message
message=b"Hello, this is a secret message."
cipher_rsa=PKCS1_OAEP.new(RSA.import_key(public_key))
cipher_text=cipher_rsa.encrypt(message)
print(f"Encrypted: {cipher_text}")
print('\n')

# Decrypt the message
cipher_rsa=PKCS1_OAEP.new(RSA.import_key(private_key))
plain_text=cipher_rsa.decrypt(cipher_text)
print(f"Decrypted: {plain_text.decode()}")
