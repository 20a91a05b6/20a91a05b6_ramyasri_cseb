##import math
##def prime_no(n):
##    count=0

##def digit_count(n):
##    count=0
##    while(n!=0):
##        n=n//10
##        count+=1
##    return count
##n=int(input())
##print(digit_count(n))        
        
##import math
##def isprime(n):
##    count=2
##    d=0
##    for i in range(2,int(math.sqrt(n))+1):
##        if(n%i==0):
##            d=n//i
##            if(d==i):
##                count+=1
##            else:
##                count+=2
##    if(count==2):
##        return True
##    else:
##        return False
##
##n=int(input())
##if(isprime(n)):
##     print("prime no")
##else:
##     print("not prime no")
##         

def isprime(n):
    fact_count=0
    for i in range(2,n):
        if(n%i==0):
            return True
        else:
            return False
        
a=int(input())
if(isprime(a)):
    print("prime number")
else:
    print("not prime number")
        
            
        
            
