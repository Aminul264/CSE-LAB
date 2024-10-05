

# if __name__=='__main__':
#     with open('input.txt','r') as infile:
#         plaintext = infile.read()
#         print(plaintext)

# import math

# def encrypt(msg, width):
#     # Add trailing spaces to make the message length a multiple of width
#     trailing_space = width - len(msg) % width
#     if trailing_space != width:
#         msg += ' ' * trailing_space

#     cipher = ""
#     for i in range(width):
#         for j in range(i, len(msg), width):
#             cipher += msg[j]
    
#     return cipher

# def decrypt(cipher, width):
#     rows = math.ceil(len(cipher) / width)
#     msg = ""
    
#     for i in range(rows):
#         for j in range(i, len(cipher), rows):
#             msg += cipher[j]
    
#     # Remove trailing spaces
#     msg = msg.rstrip()
    
#     return msg

# def main():
#     # Read width and message from the input file
#     with open('in.txt', 'r') as infile:
#         width = int(infile.readline().strip())
#         msg = infile.read().replace('\n', '')
    
#     # Encrypt and decrypt
#     cipher = encrypt(msg, width)
#     decrypted_msg = decrypt(cipher, width)
    
#     # Print and write results to the output file
#     with open('out.txt', 'w') as outfile:
#         outfile.write(f"Original message : {decrypted_msg}\n")
#         outfile.write(f"Cipher message : {cipher}\n")

#     print(f"Original message : {decrypted_msg}")
#     print(f"Cipher message : {cipher}")

def encrypt(plaintext, width):
    # to ensure its length is a multiple of the specified width
    padding =width - len(plaintext)%width
    if padding!=width:
        plaintext +=' '*padding
    cipher = ""
    for i in range(width):
        for j in range(i,len(plaintext),width):
            cipher += plaintext[j]
    
    return cipher

if __name__ == "__main__":
    
    with open('input.txt') as infile:
        # Removes any leading and trailing whitespace characters, including newlines, from the read line
        width =int(infile.readline().strip())
        # Removes all newline characters from the message.
        plaintext = infile.read().replace('\n','')
        cipher = encrypt(plaintext, width)
        print(cipher)
        
        
        
        
        
        
        
