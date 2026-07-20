class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        m=prices[0]
        a=float('-inf')
        for i in range(1,len(prices)):
            if prices[i]-m>=0:
                profit=prices[i]-m
                a=max(a,profit)
            else:
                profit=0
                a=max(a,profit)
            m=min(m,prices[i])
        return a             

            
            


        