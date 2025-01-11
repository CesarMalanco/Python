# Author: reDragonCoder

# NOTE: hashing is a one-way function that converts data into a fixed-size
# string of characters, which is typically has code. It's commonly used for
# verifying data integrity. If the hash of a message changes, t means the 
# message has been altered

# NOTE: it's computationaly infeasible to determine the original message 
# from its hash

# NOTE: hashes are used in password storage, digital signatures, etc

import hashlib

# Hash message
message="Hello, this is a secret message."
hash_object=hashlib.sha256(message.encode())
hex_dig=hash_object.hexdigest()
print(f"SHA-256 Hash: {hex_dig}")