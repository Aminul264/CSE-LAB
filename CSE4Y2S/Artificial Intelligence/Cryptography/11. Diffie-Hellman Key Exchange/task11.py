

import random

def bigmod(b,p,m):
    if p==0:
        return 1
    if p==1:
        return b%m
    elif p%2==0:
        a = (bigmod(b,p//2,m))%m
        return (a*a)%m
    else:
        a = b%m
        b= (bigmod(b,p-1,m))%m
        return (a*b)%m
    
if __name__ == '__main__':
    # Prime number and primitive root (public values)
    
    p = 13
    g = 2
    # Alice's private key
    x = random.randint(2,100)
    # Bob's private key
    y = random.randint(2,100)
    # Alice and bob computes their public key
    A = bigmod(g, x,p)
    B = bigmod(g,y,p)
    # Compute the shared secret keys
    ka = bigmod(B,x,p)
    kb = bigmod(A,y,p)
    
    # ouputs the result
    print(f'Alices secret key: {x}')
    print(f'Bobs secret key: {y}')
    print(f'Alices shared key: {ka}')
    print(f'Bobs shared key: {kb}')
    