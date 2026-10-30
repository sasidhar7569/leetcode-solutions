class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans=[]
        dici={}
        for i in nums:
            if i not in dici:
                dici[i]=1
            else:
                ans.append(i)
        for j in range(1,len(nums)+1):
            if j not in dici:
                ans.append(j)
                break
        return ans
        