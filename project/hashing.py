import hashlib

data = b'Hello, world!'
hash_value = hashlib.sha256(data).hexdigest()
# print(sizeof(hash_value))
print(len(hash_value))
