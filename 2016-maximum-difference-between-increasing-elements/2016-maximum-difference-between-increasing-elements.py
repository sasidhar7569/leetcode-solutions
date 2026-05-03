class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans=0
        min_value=nums[0]
        for i in range(1,len(nums)):
            ans=max(ans,nums[i]-min_value)
            min_value=min(min_value,nums[i])
        if ans==0:
            return -1
        else:
            return ans    

        