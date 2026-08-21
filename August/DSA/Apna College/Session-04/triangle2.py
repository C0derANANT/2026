# 9
n=int(input("Enter A Number : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=' ')
    print()

# 10
n=int(input("Enter A Number : "))
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j, end=' ')
    print()

# 11
n=int(input("Enter A Number : "))
a=0
for i in range(1,n+1):
    for j in range(i):
        a+=1
        print(a,end=' ')
    print()
