# # l1= [1, 2, 3, 2]

# # for i in l1:
# #     if l1.count(i)>1:
# #         print("True")
# #         break
# # else:
# #     print("False")

# # l1 = [4, 2, 7, 1, 8]

# # largest = l1[0]
# # for i in l1:
# #     if i > largest:
# #         largest = i

# # print(largest)


l1 = [4, 2, 7, 1, 8]

largest = l1[0]
second = float('-inf')
print(second)

for i in l1[1:]:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print(second)
print(largest)


# Moving Zeroes To The End
l1=[0, 1, 0, 3, 12]
# print(l1.count(0))
for i in range(l1.count(0)):
    l1.remove(0)
    l1.append(0)
print(l1)   