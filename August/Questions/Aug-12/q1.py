prices = {'apple': 1.5, 'banana': 0.8, 'orange': 1.5}
for i in prices:
    if prices[i]==prices[max(prices)]:
        print(i)
        break