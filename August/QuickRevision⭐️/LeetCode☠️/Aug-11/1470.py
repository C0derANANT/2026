nums = [2,5,1,3,4,7]
n = 3
x=nums[:n]
y=nums[n:]
print(x)
print(y)
l1=[]
# for x0 in x and for y0 in y:
for i in range(n):
    l1.append(x[i])
    l1.append(y[i])

print(l1)