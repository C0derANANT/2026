arr=[4,2,7,8]
print(arr)
# Q1-Calculate Sum and product
addition=0
mul=1
for item in arr:
    addition+=item
    mul*=item
print(addition)
print(mul)

# Q2-Swap max and min values 
max_index = arr.index(max(arr))
min_index = arr.index(min(arr))
arr[max_index], arr[min_index] = arr[min_index], arr[max_index]
print(arr)