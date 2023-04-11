"""
    One Time Pad cipher
"""
import random


class OneTime:

    def encrypt(self, text):
        plain  = [ord(s) for s in text]
        cipher = []
        key = []

        for i in plain:
            k = random.randint(1, 100)
            # Creating a cipher with a simple mathematical operation.
            c = (i + k) * k
            cipher.append(c)
            key.append(k)
        return cipher, key


    def decrypt(self, cipher, key): 
        plain_text = ''
        
        for c, k in zip(cipher, key):
            # The opposite of the mathematical operation in the encrypt method
            new_key = ( c // k ) - k
            plain_text += chr(new_key)
        return plain_text


    # The following method works like decrypt,
    # only the type of writing is different.
    def decrypt_2(self, cipher, key):
        plain = []
        for i in range(len(key)):
            # It shows the same behavior as the decrypt method (in another way).
            p = int((cipher[i] - key[i] ** 2) / key[i])
            plain.append(chr(p))
        result = ''.join([i for i in plain])
        return result


# To run the program, uncomment the following lines.
#onetime = OneTime()

#print(onetime.encrypt("Hello, world!"))

# We need two key (cipher and key) to decrypt the message.
#c, k = OneTime().encrypt('Hello, world!')
#print(onetime.decrypt(c, k))

