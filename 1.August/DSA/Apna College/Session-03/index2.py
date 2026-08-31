# # Prime Number Check Upto n
# n=int(input("Enter A Number : "))
# print(f'2 : PRIME')
# for i in range(3,n+1):
#     if n%i==0:
#         print(f'{i} : PRIME')
#     else:
#         print(f'{i} : NOT Prime')


# # Nested Loops
# x=int(input("Enter Number Of Stars :"))
# for i in range(5):
#     print('*'*x)


# Factorial of 'a'
factorial=1
a=int(input("Enter The Number : "))
for i in range(1,a):
    factorial*=i
    print(f"{i}",end=' x ')

print(f'{a} = {factorial*a}')