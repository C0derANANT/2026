# Diamond Patterns 
# 15
n = int(input("Enter A Number : "))
print(" " * n + "*")
for i in range(1, n):
    print(" " * (n-i) + "*" + " " * (2*i-1) + "*")
for i in range(n-2, 0, -1):
    print(" " * (n-i) + "*" + " " * (2*i-1) + "*")
print(" " * n + "*")


for i in range(n):
    print(i)

# Butterfly Pattern
# 16
n=int(input("Enter A Number : "))
for i in range(1,n+1):
    print(" *"*i+"  "*(n*2-2*i)+" *"*i)
for i in range(n,0,-1):
    print(" *"*i+"  "*(n*2-2*i)+" *"*i)