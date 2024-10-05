def encrypt(plaintext,onetimepad):
    cipher = ""
    
    for i in range(len(plaintext)):
        ch = plaintext[i]
        pad = onetimepad[i]
        
        if ch.islower():
            cipher += chr((ord(ch)-ord('a') + ord(pad)-ord('a') )%26 + ord('a'))
        elif ch.isupper():
            cipher += chr((ord(ch)-ord('A') + ord(pad)-ord('A') )%26 + ord('A'))
        else:
            cipher += ch
    return cipher
def decrypt(cipher,onetimepad):
    decipher = ""
    
    for i in range(len(cipher)):
        ch = cipher[i]
        pad = onetimepad[i]
        if ch.islower():
            decipher += chr((ord(ch)-ord('a') - ord(pad)+ord('a') )%26 + ord('a'))
        elif ch.isupper():
            decipher += chr((ord(ch)-ord('A') - ord(pad)+ord('A') )%26 + ord('A'))
        else:
            decipher += ch  # leave non-alphabetic characters unchanged
    return decipher
def main():
    with open('input.txt', 'r') as infile:
        plaintext = infile.readline().strip()
        onetimepad = infile.readline().strip()
        
    print(f'plaintext: {plaintext}')    
    cipher =encrypt(plaintext,onetimepad) 
    print(f'cipher : {cipher}')
    # decipher = decrypt(cipher,onetimepad) 
    # print(f'decipher : {decipher}')
    
if __name__ == "__main__":
    main()