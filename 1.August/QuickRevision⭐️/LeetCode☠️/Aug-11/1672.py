accounts =  [[2,8,7],[7,1,3],[1,9,5]]
new=[]
for account in accounts:
    add=0
    for i in account:
        add+=i
    new.append(add)
new.sort()
print(new[-1])