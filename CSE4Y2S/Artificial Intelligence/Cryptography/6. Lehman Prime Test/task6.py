import random

def bigmod(b,p,m):
    if p==0:
        return 1
    elif p%2==0:
        a = (bigmod(b,p//2,m))%m
        return (a*a)%m
    else:
        a = b%m
        b= (bigmod(b,p-1,m))%m
        return (a*b)%m
    
def lehman_test(p,t):
    if p<=1 or p%2==0:
        return False
    if p==2 or p==3:
        return True
    
    # repeat t times
    for _ in range(t):
        # choose a random number 2<=a<=p-1
        a = random.randint(2,p-1)
         # Calculate a^(p-1)/2 % p
        result = bigmod(a,(p-1)//2,p)
        if result != -1 and result!=p-1 and result!=1:
            return False
    return True
        
        
    
if __name__ == "__main__":
    p = int(input("Entera a number p: "))
    t = int(input("Enter a number for iteration t: "))
    
    if(lehman_test(p,t)):
        print(f"{p} is a prime number")
    else:
        print(f'{p} is not a prime number')
