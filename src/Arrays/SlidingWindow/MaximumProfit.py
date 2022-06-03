def maxProfit(prices) -> int:
        l = 0
        maxProfit = 0
        for r in range(1, len(prices)):
            print(l,r)
            if prices[l] < prices[r]:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            else:
                l = r
            r+=1
        return maxProfit
    
print(maxProfit([7,1,5,3,6,4]))