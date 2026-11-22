class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a=prices[0]
        b=float('-inf')
        i=1
        while i<len(prices):
            profit=prices[i]-a
            b=max(b,profit)

            a=min(a,prices[i])
            i+=1
        if b<=0:
            return 0
        else:
            return b     



           


        