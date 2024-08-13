a=int(input("Enter num: "))
prime=False
if a==1:
    print("not a prime")
elif a>0:
    for i in range(2,a):
        if(a%i==0):
            prime=True
            break

    if prime :
        print("not a prime" )
    else:
        print("prime")
