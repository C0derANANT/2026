# Q7
#    1
#   12
#  123
# 1234
#12345
n=int(input("Enter A Number : "))
num=''
for i in range(1,n+1):
    num+=str(i)
    print(" "*(n-len(num))+num)

# Q8
#     *
#    ***
#   *****
#  *******
# *********
n=int(input("Enter A Number : "))
for i in range(n):
    print(" "*(n-i)+"*"*(i*2+1))
