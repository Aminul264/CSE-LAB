def encrypt(plaintext, width):
    # to ensure its length is a multiple of the specified width
    padding =width - len(plaintext)%width
    plaintext +='-'*padding # padding by -
    cipher = ""
    for i in range(width):
        for j in range(i,len(plaintext),width):
            cipher += plaintext[j]
    return cipher
def decrypt(cipher, width):
    plaintext = ""
    row = int(len(cipher)/width)
    for i in range(row):
        for j in range(i, len(cipher), row):
            plaintext += cipher[j]
    return plaintext
    
if __name__ == "__main__":
    
    with open('input.txt') as infile:
        # Removes any leading and trailing whitespace characters, including newlines, from the read line
        width =int(infile.readline().strip())
        # Removes all newline characters from the message.
        plaintext = infile.read().replace('\n','')
        cipher = encrypt(plaintext, width)
        print(cipher.replace('-',''))
        print(decrypt(cipher, width).replace('-',''))
        
        
        
        
        
        
        
