from string import ascii_letters


'''
    The action of a Caesar cipher is to replace each plaintext letter
    with a different one a fixed number of places down the alphabet.
'''

def encrypt(string, key):
    
    alpha  = ascii_letters
    result = ''

    for ch in string:
        if ch not in alpha:
            result += ch
        else:
            index   = alpha.index(ch)
            new_key = (index + key) % len(alpha)
            result += alpha[new_key]

    return result 


def decrypt(string, key):
    '''
    We use the above encrypt function to decrypt the string again,
    with the difference that we only multiply the key by -1.
    '''
    
    key *= -1 
    return encrypt(string, key)


def brute_force(string):
    '''  
    Use this method to crack the password. It first takes the encrypted string
    as an argument and then outputs a dictionary containing the decrypted values with the same key.
    The most human readable value(string) can be taken as the result.
    '''
    
    brute_force_data = {}
    result = ''
    alpha  = ascii_letters
    key = 1

    while key <= len(alpha):
        result = decrypt(string, key)
        brute_force_data[key] = result
        result = ''
        key += 1
    return brute_force_data


# To run the program, uncomment the following lines.

#print(encrypt("Mohammad.Jalalnia@gmail.com", 5))
#print(decrypt("Rtmfrrfi.Ofqfqsnf@lrfnq.htr", 5))
#print(brute_force('Rtmfrrfi.Ofqfqsnf@lrfnq.htr'))

