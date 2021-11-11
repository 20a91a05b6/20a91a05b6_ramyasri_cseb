##l=[]
##n=int(input())
##for i in range(n+1):
##    ele=int(input())
##    l.append(ele)
##print(l)    


##l=[int(i) for i in input().split()]
##print(l)

'''l=[1,2,3,4,5]
n=int(input())
for i in range(0,n):
    a=l[0]  
    l.pop(0)
    l.append(a)
print(l)'''
l=[int(i) for i in input().split()]
n=int(input())
while(n%len(l)):
    x=l[0]
    a=len(l)
    for i in range(1,a):
        l[i-1]=l[i]
    l[a-1]=x
    n=n-1
print(l)


