n = int(input("Enter A Number : "))
l1 = [[1]]

for i in range(1, n):
    l2 = [1]
    for j in range(len(l1[-1]) - 1):
        l2.append(l1[-1][j] + l1[-1][j + 1])
    l2.append(1)
    l1.append(l2)

print(l1)
for item in l1:
    print(item)