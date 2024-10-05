def encrypt(text,shift):
    encrypted_text = ""
    for ch in text:
        if ch.islower():
          encrypted_text+=chr((ord(ch)-ord('a')+shift)%26 + ord('a'))
        elif ch.isupper():
            encrypted_text+= chr((ord(ch)-ord('A')+shift)%26 + ord('A'))
        else:
            encrypted_text+=ch        
    return encrypted_text;

def decrypt(text,shift):
    return encrypt(text,-shift)
    
if __name__ == "__main__":
    
    # file input
    with open('input.txt','r') as infile:
        shift = int(infile.readline().strip())
    with open('input.txt','r') as infile:
        plaintext = infile.read()
         
    ecrypted_text=encrypt(plaintext,shift)
    print(f"Encrypted text: {ecrypted_text}")
    
    decrypted_text=decrypt(ecrypted_text,shift)
    print(f"Decrypted text: {decrypted_text}")
    
    