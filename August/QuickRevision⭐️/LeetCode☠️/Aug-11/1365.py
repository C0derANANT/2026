nums = [7,7,7,7]
l1=[]
for i in nums :
    additon=0
    for j in nums:
        additon+=i>j
    l1.append(additon)
print(l1)