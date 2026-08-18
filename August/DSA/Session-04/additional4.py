# Q9
# *****
# *   *
# *   *
# *   *
# *****

# n=int(input("Enter A Number : "))
# print("*"*n)
# for i in range(n-2):
#     print("*"+" "*(n-2)+"*")
# print("*"*n)


# Q10
#    *
#   * *
#  *   *
# *     *
#*********
n=int(input("Enter A Number : "))
print(" "*(n-1)+"*")
for i in range(1,n-1):
    print(" "*(n-i)+"*"+" "*i+"*")
print("*"*(2*n-1))

