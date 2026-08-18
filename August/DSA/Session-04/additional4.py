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
print()
print(" "*(n-1)+"*")
count=0
for i in range(n-2,0,-1):
    print(" "*i+"*"+' '*(count*2+1)+"*")
    count+=1
print("*"*(2*n-1))
print()