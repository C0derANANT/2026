# Pascal Triangle
n = int(input("Enter A Number : "))
l1 = [[1]]

for i in range(n - 1):
    l2 = [1]
    for j in range(len(l1[i]) - 1):
        l2.append(l1[i][j] + l1[i][j + 1])
    l2.append(1)
    l1.append(l2)
for items in l1:
    print(" "*(n - len(items)), end="")
    print(items)

# # print(l1)


# batch size zyada hoga toh gpu zyada use hoga aur memory bhi zyada use hogi. Agar batch size chhota hoga toh gpu kam use hoga aur memory bhi kam use hogi.
# toh better konsa h bcoz ek mein load zyaada hoga aur dusre mein load kam hoga.but dusre me time km hofa