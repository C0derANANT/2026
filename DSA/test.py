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

# print(l1)