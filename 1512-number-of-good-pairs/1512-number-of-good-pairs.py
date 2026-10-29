class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        dici={}
        for i in nums:
            if i not in dici:
                dici[i]=1
            else:
                dici[i]+=1
        b=0
        for j in dici:
            a=dici[j]
            b+=(a*(a-1)//2)
        return b

        