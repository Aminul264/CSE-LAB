def encryption(msg, width):
    ans = ""
    for i in range(width):
        for j in range(i, len(msg), width):
            ans += msg[j]
    return ans

def decryption(cipher, width):
    height = len(cipher) // width
    extra = len(cipher) % width

    # Create a list to hold the decrypted message
    ans = [""] * len(cipher)
    idx = 0

    # Distribute the characters from the cipher into the correct positions
    for col in range(width):
        col_height = height + 1 if col < extra else height
        for row in range(col_height):
            ans[row * width + col] = cipher[idx]
            idx += 1

    return ''.join(ans)




if __name__ == "__main__":
    with open('example.txt', 'r') as infile:
        plaintext = infile.readline().strip()
        width = 10  # Define the width for encryption

    print(f"Original Text: {plaintext}")
    
    # Perform double encryption
    en_text = encryption(encryption(plaintext, width), width)
    print(f"Cipher Text: {en_text}")
    
    # Perform double decryption
    dec_text = decryption(decryption(en_text, width), width)
    print(f"Decrypted Text: {dec_text}")

