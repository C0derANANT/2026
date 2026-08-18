# Square Pattern
n=int(input("ENTER A NUMBER : "))
pattern=''
for i in range(n):
    pattern+=str(i+1)+" "
pattern+='\n'
print(pattern*n)