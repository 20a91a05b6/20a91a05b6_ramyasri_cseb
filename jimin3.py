def count(n):
    d_count=0
    while(n):
        n=n//10
        d_count+=1
    return d_count
def armstrong(n):
    res=0
    
    copy=n
    temp=n
    
    while(temp):
        r=temp%10
        res=res+(r**count(n))
        temp=temp//10
    if(res==copy):
        print("armstrong no")
    else:
        print("not armstrong no")
n=int(input())
armstrong(n)
