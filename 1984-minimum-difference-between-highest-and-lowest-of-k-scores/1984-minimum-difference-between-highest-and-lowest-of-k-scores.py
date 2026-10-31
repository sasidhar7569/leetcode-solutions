class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort(reverse=True)
        l=0
        ans=float("inf")

        for r in range(len(nums)):
            if(r-l==k):
                l+=1
            if(r-l+1==k):
                ans=min(ans,nums[l]-nums[r])
        return ans
        