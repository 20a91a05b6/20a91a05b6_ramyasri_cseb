##n=int(input())
##num=0
##
##while(n):
##    r=n%10
##    num=num+(r*r)
##    n=n//10
##    if(n==0):
##        n=num
##        num=0
##        if(n>=1 and n<10):
##            break;
##if(n==1):
##    print("happy number")
##else:
##    print("not happy number")
    
##n=int(input())
##res=0
##d_count=0
##copy=n
##temp=n
##while(n):
##    n=n//10
##    d_count+=1
##while(temp):
##    r=temp%10
##    res=res+(r**d_count)
##    temp=temp//10
##if(res==copy):
##    print("armstrong no")
##else:
##    print("not armstrong no")
##    
##

def armstrong(n):
    res=0
    d_count=0
    copy=n
    temp=n
    while(n):
        n=n//10
        d_count+=1
    while(temp):
        r=temp%10
        res=res+(r**d_count)
        temp=temp//10
    if(res==copy):
        print("armstrong no")
    else:
        print("not armstrong no")
n=int(input())
armstrong(n)

    
