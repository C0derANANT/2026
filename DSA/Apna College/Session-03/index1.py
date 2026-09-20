# Sum Of Numbers Upto n
n=int(input("Enter a number: "))
sum=0
for i in range(n):
    sum+=i+1
print("Sum of numbers upto",n,"is:",sum)

# Sum Of All Odd Numbers Upto n
odd_sum=0
for i in range(n):
    if (i+1)%2!=0:
        odd_sum+=i+1
print(odd_sum)

# Sum Of All Odd Numbers Upto n
j=0
odd_sum=0
while j <n:
    j+=1
    if j%2!=0:
        odd_sum+=j
print(odd_sum)

# Sum Of All Even Numbers Upto n
even_sum=0
for i in range(n):
    if (i+1)%2==0:
        even_sum+=i+1
print(even_sum)