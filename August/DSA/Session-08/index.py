# Learning Array
l1=[4,5,32,423,965,-12,-1245362]
print(f'\n\nMaximum Value In List : {max(l1)}, Which is at index {l1.index(max(l1))}\n\n')
print(f'Minimum Value In List : {min(l1)}, Which is at index {l1.index(min(l1))}\n\n')

# Loops In Array
l2=[]
n=int(input("Enter A Number : "))
for i in range(n):
    l2.append((i+1)*2)
for item in l2:
    print(item,end=' ')
print()


# Linear Search
arr=[4,2,7,8,1,5]
target=8
for i in arr:
    if target==i:
        print(i)
        break
else:
    print(-1)
    
# In-Built
if target in arr:
    print(arr.index(target))
else:
    print(-1)