n = int(input())
leap=False
if n%400==0:
    leap=True
elif n%4==0 and n%100!=0:
    leap=True
print(leap)