prices = [7,6,5,4,10,1]

l1=[]
while True:
    minimum=prices.index(min(prices))
    if minimum==len(prices)-1:
        prices.remove(min(prices))
    else:
        break
for i in prices[minimum+1:]:
    l1.append(i)
profit=max(l1)-min(prices)
# if profit>0:
print(profit)

