
def encrypt(plaintext,shift):
    cipher =""
    for ch in plaintext:
        if ch.islower():
            cipher += chr((ord(ch)-ord('a')+shift)%26 + ord('a'))
        elif ch.isupper():
            cipher += chr(((ord(ch)-ord('A')+shift)%26)+ord('A'))
        else:
            cipher += ch
    return cipher
def decrypt(cipher,shift):
    return encrypt(cipher,-shift)         
def main():
    with open('input.txt','r') as infile:
        shift = int(infile.readline().strip())
        plaintext = infile.read().strip()
    print(f'plaintest:\n {plaintext}')
    cipher = encrypt(plaintext,shift)
    print(f'cipher: \n{cipher}')
    decipher = decrypt(cipher,shift)
    print(f'decipher: \n{decipher}')
            
if __name__ == '__main__':
    main()