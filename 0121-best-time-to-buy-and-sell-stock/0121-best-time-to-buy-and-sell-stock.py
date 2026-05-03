class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val=prices[0]
        ans=0
        for i in range(1,len(prices)):
            ans=max(ans,(prices[i]-min_val))
            min_val=min(min_val,prices[i])
        return ans    