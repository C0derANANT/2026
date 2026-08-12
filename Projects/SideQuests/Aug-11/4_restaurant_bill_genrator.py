n1=int(input("Enter Price Of Item 1: "))
n2=int(input("Enter Price Of Item 2: "))
n3=int(input("Enter Price Of Item 3: "))
n4=int(input("Enter Price Of Item 4: "))
n5=int(input("Enter Price Of Item 5: "))

l1=[n1,n2,n3,n4,n5]
total=sum(l1)
highest_price=max(l1)
lowest_price=min(l1)

if total>=2000:
    price_after_discount=total*0.8
elif total>=1000:
    price_after_discount=total*0.9
else:
    price_after_discount=total

tax=price_after_discount*.05   # 5 Percent GST
price_after_tax=price_after_discount+tax
print("Individual Prices: ",l1)
print("Total Price: ",total)
print("Price After Discount: ",price_after_discount)
print("Tax: ",tax)
print("Price After Tax: ",price_after_tax)
print("Final Price: ",price_after_tax)
