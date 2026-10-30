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

# s=set()
# miss=0
# dup=0
# for i in range(len(nums)):
#   if nums[i] not in s:
#     s.add(nums[i])
#   else:
#     dup=nums[i]
# for j in range(1,len(nums)+1):
#   if j not in s:
#     miss=j
#     break
# print([dup,miss])
        