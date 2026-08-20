# Square Pattern

# 1
n=int(input("ENTER A NUMBER : "))
for i in range(n):
    for j in range(1,n+1):
        print(j,end=' ')
    print()

# 2
# For n=3
# 1 2 3
# 4 5 6 
# 7 8 9
n=int(input("Enter A Number : "))
for i in range(n):
    print("* "*n)