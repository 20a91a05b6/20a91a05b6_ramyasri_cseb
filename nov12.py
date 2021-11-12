###sum of odd numbers
##l=[12,23,57,108,3,4]
##sum=0
##for i in l:
##    if(i%2!=0):
##        sum=sum+i
##print(sum)

'''sum of 1st five odd numbers'''
##n=int(input())
##sum=0
##for i in range(1,2*n+1,2):
##    sum=sum+i
##print(sum)    
####or    
##n=int(input())
##print(n*n)

'''sum of 1st 5 odd no'''
##n=int(input())
##print(n*(n+1))

#find count of even numbers with evenindex 
##l=[2,3,6,7,8,10,9]
##count=0
##for i in range(0,len(l)):
##     if(i%2==0 and l[i]%2==0 and i!=0):
##         count+=1
##        
##print(count)

'''print running sum of an array'''
l=[1,2,3,4]
a=[]
sum=0
for i in range(0,len(l)):
    sum=sum+l[i]
    a.append(sum)
print(a)
    
