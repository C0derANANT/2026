prices = [10,1,1,6]
discount_prices=[]
valid=False
for i in range(len(prices)):
    valid=False
    for j in range(i+1,len(prices)):
        discount=prices[i]-prices[j]
        if discount>=0:
            discount_prices.append(discount)
            valid=True
            break
    if not valid:
        discount_prices.append(prices[i])      
print(discount_prices)
