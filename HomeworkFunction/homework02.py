def isprime(num):
    if num> 1:  
        for n in range(2,num):  
            if (num % n) == 0:  
                return False
        return True
    else:
        return False
print(isprime(18))
print(isprime(3))

#Another way
def isprime(num):
    for n in range(2,int(num**1/2)+1):
        if num%n==0:
            return False
    return True
print(isprime(1))
print(isprime(7))