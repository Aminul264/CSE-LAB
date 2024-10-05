
en_dictionary = {}
dec_dictionary = {}

def create_dictionary(dictionary):
    for line in dictionary:
        w1,w2 = line.strip().split(' ')
        en_dictionary[w1] = w2
        dec_dictionary[w2] = w1
def encrypt(msg,block_size):
    cipher = ""
    word=""
    for ch in msg:
        if ch.isalpha():
            word += ch.upper()
            # if len(word) == block_size:
            if word in  en_dictionary:
                cipher += en_dictionary[word]
                word = ""
        else:
            cipher +=ch
    return cipher
    
def decrypt(cipher,block_size):
    decipher = ""
    word= ""
    for ch in cipher:
        if ch.isalpha():
            word+=ch.upper()
            # if len(word)==block_size:
            if word in dec_dictionary:
                decipher+=dec_dictionary[word]
                word = ""
        else:
            decipher+=ch    
    return decipher

if __name__ == "__main__":
    
    with open('input.txt') as infile:
        block_size =int(infile.readline().strip())
        msg = infile.readline().strip()
    with open('dictionary.txt', 'r') as infile:
        dictionary = infile.readlines()
    create_dictionary(dictionary)
    # print(en_dictionary)
    # print(dec_dictionary)
    cipher = encrypt(msg,block_size)
    print(f'cipher: {cipher}')
    decipher = decrypt(cipher,block_size)
    print(f'decipher: {decipher}')
    
    
        
    
        
        
        
        
        
        
        
