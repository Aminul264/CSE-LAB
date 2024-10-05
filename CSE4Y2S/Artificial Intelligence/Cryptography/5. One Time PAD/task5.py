def encrypt(plaintext,random_string):
    cipher = ""
    for i in range(len(plaintext)):
        ch = plaintext[i]
        r = random_string[i]
        if ch.islower():
            cipher += chr((ord(ch)-ord('a')+ ord(r)-ord('a'))%26 + ord('a'))
        elif ch.isupper():
            cipher += chr((ord(ch)-ord('A')+ ord(r)-ord('A'))%26 + ord('A'))
        else:
            cipher += ch
    return cipher
def decrypt(cipher, random_string):
    decipher = ""
    for i in range(len(cipher)):
        ch = cipher[i]
        r = random_string[i]
        if ch.islower():
            decipher += chr((ord(ch)-ord('a')-ord(r)+ord('a'))%26 + ord('a'))
        elif ch.isupper():
            decipher += chr((ord(ch)-ord('A')-ord(r)+ord('A'))%26 + ord('A'))
        else:
            decipher += ch
    return decipher
if __name__ == "__main__":
    with open('input.txt', 'r') as infile:
        plaintext = infile.readline().strip()
        onetimepad = infile.readline().strip()
    
    cipher = encrypt(plaintext, onetimepad)
    print(cipher)
    print(decrypt(cipher, onetimepad))
