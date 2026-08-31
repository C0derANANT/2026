# Q1
# *
# **
# ***
# ****
# *****
n=int(input("Enter A Number : "))
for i in range(1,n+1):
    print("*"*i)



# Q2
# 1
# 12
# 123
# 1234
# 12345
n=int(input("Enter A Number : "))
pattern=''
for i in range(1,n+1):
    pattern+=str(i)
    print(pattern)