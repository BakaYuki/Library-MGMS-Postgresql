import hashlib

data = b'Hello, world!'
hash_value1 = hashlib.sha256(data).hexdigest()
# print(sizeof(hash_value))

data2 = b'Hello, world!'
hash_value2 = hashlib.sha256(data2).hexdigest()
if hash_value1 == hash_value2 :
    print("here") 

print(hash_value1)
print(hash_value2)