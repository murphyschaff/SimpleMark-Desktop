from miscFunctions import *
import random

message = 'this is message'
key = keyGen(len(message))

cipher = encode(key, message)
decoded = decrypt(key, cipher)
print(cipher)
print(decoded)

message = '\\0x5f\\0x88\\0x6e\\0x1e\\0x33\\0x34\\0x99\\0x18\\0xf5\\0x47\\0x6\\0x29\\0x45\\0x6d\\0xf3\\0xfe\\0xd1\\0x29\\0xc7\\0xb8\\0xb4\\0x82'
key = '\\0x2f\\0x58\\0x36\\0xab\\0xd2\\0xd0\\0x33\\0xb7\\0x82\\0xe3\\0xa0\\0xf3\\0xff\\0x67\\0xf5\\0x74\\0xe4\\0x70\\0x56\\0x4d\\0x8c\\0x97'

print(getEncodedLength(key,message))

'''
#testing correctness on encryption function
for i in range(100000):
    strLen = random.randint(1, 100)
    message = ''
    for _ in range(strLen):
        message += chr(random.randint(0,255))
    
    key = keyGen(strLen)

    cipher = encode(key, message)
    decipher = decrypt(key,  cipher)

    if message != decipher:
        print(f'test {i+1} incorrect value.\nmessage: {message}\ncipher: {cipher}\ndecoded: {decipher}')
        break
    else:
        print(f'test {i+1} passed')
        '''