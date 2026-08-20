# # 12
# alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# n=int(input("Enter A Number : "))
# for i in range(0,n):
#     for j in range(i,-1,-1):
#         print(alphabets[j], end=' ')
#     print()


# # 13
# n=int(input("Enter A Number : "))
# x=n
# for i in range(n):
#     print("  "*(n-x) +f"{str(i+1)} "*x)
#     x-=1


# 14
n=int(input("Enter A Number : "))
for x in range(1,n+1):
    print("  "*(n-x),end='')
    for i in range(1,x):
        print(i,end=' ')
    for j in range(x,0,-1):
        print(j,end=' ')
    print()
    