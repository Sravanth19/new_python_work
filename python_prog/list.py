num=int(input("Enter the size of list :"))
list=[]
for i in range(num):
    ele=int(input("Enter the {} element :".format(i)))

    list.append(ele)

print(max(list))
