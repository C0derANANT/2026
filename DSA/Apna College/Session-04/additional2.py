# Q5
# 12345
# 1234
# 123
# 12
# 1
# num=''
# n=int(input("Enter A Number : "))
# for i in range(1,n+1):
#     num+=str(i)
# print(num)
# while len(num)>0:
#     num=num[:-1]
#     print(num)


# Q6
#    *
#   **
#  ***
# ****
#*****
n=int(input("Enter A Number : "))
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)