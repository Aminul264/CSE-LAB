def encrypt(plaintext, width):
    # Ensure the length is a multiple of the width by adding padding (only once)
    padding = width - len(plaintext) % width
    if padding != 0 and padding != width:  # Add padding only if needed
        plaintext += '-' * padding  # Padding with '-'
    
    cipher = ""
    for i in range(width):
        for j in range(i, len(plaintext), width):
            cipher += plaintext[j]
    
    return cipher

def decrypt(cipher, width):
    plaintext = ""
    row = len(cipher) // width
    for i in range(row):
        for j in range(i, len(cipher), row):
            plaintext += cipher[j]
    return plaintext

if __name__ == "__main__":
    with open('input.txt') as infile:
        # Read and process input
        width = int(infile.readline().strip())
        plaintext = infile.read().replace('\n', '')  # Remove newlines from the message

        # First round of encryption (first transposition)
        cipher1 = encrypt(plaintext, width)
        
        # Second round of encryption (double transposition)
        cipher2= encrypt(cipher1, width)
        print("Double Encrypted (without padding):", cipher2.replace('-', ''))

        # First round of decryption
        decipher1 = decrypt(cipher2, width)
        
        # Second round of decryption (double transposition)
        decipher2 = decrypt(decipher1, width)
        
        # Output the original plaintext
        print("Decrypted (Original Plaintext):", decipher2.replace('-', ''))
