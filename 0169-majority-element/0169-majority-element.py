class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # dici={}
        n=len(nums)
        # for i in nums:
        #     if i in dici:
        #         dici[i]+=1
        #     else:
        #         dici[i]=1
        # for j in dici:
        #     if dici[j]>(n/2):
        #         return j    
        nums.sort()
        return nums[n//2]       
