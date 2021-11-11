##for i in range(1,6):
##    for j in range(1,6):
##        print(j,end="")
##    print()

##a=5
##for i in range(1,6):
##    
##    for j in range(1,6):
##        print(a,end="")
##    a-=1
##    print()

##for i in range(1,6):
##    for j in range(1,i+1):
##        print(j,end="")
##    print()
    
##for i in range(1,6):
##    for j in range(1,6-i):
##        print(" ",end="")
##    for k in range(1,i+1):
##        print(i,end=" ")
##    print()

####for i in range(5,0,-1):
####    for j in range(0,5-i):
####        print(" ",end="")
####    for k in range(1,i+1):
####        print(i,end=" ")
####        
####    print()
r_count=0
n=int(input())
i=1
while(True):
    print(i,end="")
    i+=1
    if(i==n+1):
        print()
        i=1
        r_count+=1
        if(r_count==n):
            break
    
