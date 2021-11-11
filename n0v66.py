##        
##l=0
##m=0
##r=len(li)-1
##while(m<=r):
##    if(li[m]==1):
##        m+=1
##    elif(li[m]==0):
##        li[l],li[m]=li[m],li[l]
##        l+=1
##        m+=1
##    else:
##        li[r],li[m]=li[m],li[r]
##        r-=1
##        
##print(li)        
##        l=[int(i) for i in input().split()]
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

##
l=[1,7,10,13,15,16,17]
t=int(input())
 
for i in l:
    if(i==t):
        print("element found")
        break
else:
    print(-1)

          
