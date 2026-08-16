n=int(input("Enter A Number : "))
addition=0
for i in range(1,n+1):
    addition+=i
print("Sum of First",n,"Natural Numbers is :",addition)
print("--------------------------------")
for i in range(2,n+1):
    for j in range(1,11):
        print(i,"x",j,"=",i*j)
    print('\n\t\t\t')