##l=[int(i) for i in input().split()]
##i=0
##a=len(l)-1
##while(a):
##    if(l[i]==1):
##        x=l.pop(i)
##        l.append(x)
##    else:
##        i+=1
##    a=a-1
##print(l)        

l=[1,0,2,0,1,2]
for i in range(0,len(l)+1):
    for j in range(i+1,len(l)):
        if(l[i]>l[j]):
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
        else:
            j+=1
            
print(l)        

