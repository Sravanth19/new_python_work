a=int(input("enter number for fibonacci"))
first=0
second=1
print("{}\n{}".format(first,second))
for i in range(0,a-2):
    third=first+second
    print(third)
    first=second
    second=third
print(a)
