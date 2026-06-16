class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dici={}
        for i in range(len(nums)):
            ans=target-nums[i]
            if ans in dici:
                return [dici[ans],i]
                break
            dici[nums[i]]=i    