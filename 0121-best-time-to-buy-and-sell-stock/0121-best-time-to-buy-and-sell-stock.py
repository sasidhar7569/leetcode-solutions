class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_val=prices[0]
        ans=0
        for i in range(1,len(prices)):
            if min_val>prices[i]:
                min_val=prices[i]
            k=prices[i]-min_val
            if k>ans:
                ans=k
        return ans
        

        