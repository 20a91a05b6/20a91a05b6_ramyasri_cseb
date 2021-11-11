l = [2,3,1,2,4,3]
x=0
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if(l[i]==l[j]):
            print(l[i],end="")
            x+=1
   
if x==0:
    print(-1)
