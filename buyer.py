def maxprofit(price,n):
    profit=[0]*n
max-price=price[i]:
profit[i]=max(profit[i+1]),max_profit-price[i]
min_price=price[0]
for i in range(1,n):
        if price[i]<min_price[i]:
         profit=max(profit[i-1],profit[i]+(profit[i]-min_price))
        result=profit[n-1]
        return result
price=[2,5,19,25,30,6]
print("maximum profit is",maxprofit(price,len(price)))
