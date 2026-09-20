# # 3
alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n=int(input("Enter A Number : "))
for j in range(n):
    for i in range(n):
        print(alphabets[i],end=' ')
    print()

# 4
n=int(input("Enter A Number : "))
for i in range(1,n+1):
    for j in range(n*(i-1)+1,n*i+1):
        print(j,end=' ')
    print()

# 5

alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n=int(input("Enter A Number : "))
for j in range(0,n):
    for i in range(n*j,n*(j+1)):
        print(alphabets[i],end=' ')
    print()