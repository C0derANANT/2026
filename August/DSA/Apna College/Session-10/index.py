# Kadane's Algorithm
# ALL the subarrays

# l1 = [1, 2, 3, 4, 5]
l1=[3,-4,5,4,-1,7,-8]
all_arrays = []
all_sum = []

for i in range(len(l1)):
    for j in range(i, len(l1)):
        print(l1[i:j+1],end=' ')
        all_arrays.append(l1[i:j+1])
    print()

# print(all_arrays)

for arr in all_arrays:
    all_sum.append(sum(arr))
                                                         
# print(all_sum)
print(f"\n\nThe Substring With Max Sum Is  : {all_arrays[all_sum.index(max(all_sum))]}\n\n")












