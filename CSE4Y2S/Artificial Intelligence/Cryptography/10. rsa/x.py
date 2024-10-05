import math
import random

def generate_e(phi):
    while True:
        x =  random.randint(2,phi-1)
        if math.gcd(x,phi)==1:
            return x
    return -1
    
def mod_inverse(e,phi):
    for i in range(1,phi):
        if e*i % phi==1:
            return i
    return -1
def key_generator(p,q):
    n =  p*q;
    phi = (p-1)*(q-1)
    e = generate_e(phi)
    d = mod_inverse(e,phi)
    return (e,d)
def big_mod(m,p,n):
    if p==0:
        return 1
    if p==1:
        return m%n
    if p%2==0:
        half = big_mod(m,p//2,n)%n
        return (half*half)%n
    else:
        a = m%n
        b = big_mod(m,p-1,n)%n
        return (a*b)%n
        
def rsa_encryption(msg,e,n):
    blocks =  [msg[i:i+3] for i in range (0,len(msg),3)]
    cipher = []
    for block in blocks:
        m = int(block)
        cipher.append(big_mod(m,e,n))
    return cipher
         
    
def rsa_decryption(cipher,d,n):
    decipher = ''
    for c in cipher:
        decipher += str(big_mod(c,d,n))
    return decipher    
def main():
    with open('input.txt') as infile:
        p = int(infile.readline().strip())
        q = int(infile.readline().strip())
        msg = infile.readline().strip()
    e,d = key_generator(p,q)
    print(f'public key: {e,p*q} \n private key: {d,p*q}')
    print(f'message: {msg}')
    cipher = rsa_encryption(msg,e,p*q)
    tmp = ''.join(str(c) for c in cipher)
    print(f'cipher: {tmp}')
    decipher = rsa_decryption(cipher,d,p*q)
    print(f'decipher: {decipher}')
    

    
    
        
if __name__ == '__main__':
    main()