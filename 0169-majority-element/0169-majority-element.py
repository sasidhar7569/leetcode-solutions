class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        dici={}
        for i in nums:
            if i not in dici:
                dici[i]=1
            else:
                dici[i]+=1
        for j in dici:
            if dici[j]>len(nums)//2:
                return j
            
        