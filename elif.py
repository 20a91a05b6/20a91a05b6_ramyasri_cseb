a=int(input())
print("total amount is",a)
if a<1000:
    print("amount paid is",a)
elif 1000<=a<=2000:
    d=(a*10)/100
    print("discount is",d)
    b=a-d
    print("amount paid is",b)
elif 2000<a<=3000:
    d=(a*20)/100
    print("discount is",d)
    b=a-d
    print("amount paid is ",b)
elif 3000<a<=5000:
    d=(a*30)/100
    print("discount is ",d)
    b=a-d
    print("amount paid is",b)
elif a>5000:
    d=(a*40)/100
    print("discoount is ",d)
    b=a-d
    print("amount paid is ",b)
    
