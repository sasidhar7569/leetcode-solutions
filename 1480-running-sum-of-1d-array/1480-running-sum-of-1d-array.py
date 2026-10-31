class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        temp=0
        ans=[]
        for i in nums:
            temp+=i
            ans.append(temp)
        return ans
        