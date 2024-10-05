
import math
import random
def generate_encryption_key(phi):
    
    while True:
        x = random.randint(2,phi-1)
        if math.gcd(x, phi)==1:
            return x
def generate_decryption_key(e,phi):
    for i in range(1,phi):
        if (e*i % phi) ==1:
            return i
        
def generate_keys(p,q):
    n = p*q
    phi = (p-1)*(q-1)
    e = generate_encryption_key(phi)
    d = generate_decryption_key(e,phi)
    return ((e,p*q),(d,p*q))
    # return (79, 3337), (1019, 3337)
    
def big_mod(m,p,n):
    if p == 0:
        return 1
    if p == 1:
        return m%n
    if p%2==0:
        half = big_mod(m,p//2,n)%n
        return (half*half)%n
    else:
        a = m%n
        b = big_mod(m,p-1,n)%n
        return (a*b)%n
def rsa_encrypt(msg,e,n,block_size):
    cipher = []
    blocks = [msg[i:i+block_size] for i in range(0,len(msg),block_size)]
    
    for block in blocks:
        block = int(block)
        cipher.append(int(big_mod(block,e,n)))
    return cipher
def rsa_decrypt(cipher,d,n,block_size):
    
    decipher = []
    for block in cipher:
        b = big_mod(block,d,n)
        # decipher.append(f'{b:0{block_size}d}')
        decipher.append(b)
        
    return decipher
    
def main():
    with open('input.txt','r') as infile:
        p = int(infile.readline().strip())
        q = int(infile.readline().strip())
        message = infile.read().strip().replace('\n','')
    
    # Generate RSA keys
    (e,n),(d,n) = generate_keys(p,q)
    print(f'public key: {e,n} \nprivate key: {d,n}')
    cipher = rsa_encrypt(message,e,n,block_size=3)
    decipher = rsa_decrypt(cipher,d,n,block_size=3)
    
    cipher = ''.join(str(block) for block in cipher)
    decipher = ''.join(str(block) for block  in decipher)
    print(f' cipher: {cipher}')
    print(f' decipher:{decipher}')
    print(f'original:{message}')
    
    
if __name__ =="__main__":
    # this code will work only  when the  input message  contains non zeros digits
    main()