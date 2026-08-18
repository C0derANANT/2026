# Square Pattern

# 1
# n=int(input("ENTER A NUMBER : "))
# pattern=''
# for i in range(n):
#     pattern+=str(i+1)+" "
# pattern+='\n'
# print(pattern*n)

# 2
# 1 2 3
# 4 5 6 
# 7 8 9

n=int(input("Enter A Number : "))
for i in range(0,n):
    for j in range(n*i+1,n*(i+1)+1):
        print(j,end=' ')
    print()
