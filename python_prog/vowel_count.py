string=str(input("Enter string to calculate vowels: "))
vol_count=0
string=string.lower()
for char in string:
    if char in 'aeiou':
        vol_count+=1
print("no of vowels:",vol_count)
