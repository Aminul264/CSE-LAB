
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

def robin_test(p,t):
    if p<=1 or p%2==0:
        return False
    if p==2 or p==3:
        return True
    # Write p-1 as 2^s * m
    m=p-1
    s=0
    while m%2==0:
        m/=2
        s+=1
    
    for _ in range(t):
        a = random.randint(2,p-1)
        # a^m mod p
        z = bigmod(a,m,p)
        if z==1 or z==p-1:
            continue
        # Check if squaring can produce p-1
        for _ in range(s-1):
            z = z*z % p
            if z ==p-1:
                break;
            if z == 1:
                return False  
        else:
            return False
    return True

if __name__ == "__main__":
    p = int(input("Entera a number p: "))
    t = int(input("Enter a number for iteration t: "))
    
    if(robin_test(p,t)):
        print(f"{p} is a prime number")
    else:
        print(f'{p} is not a prime number')
