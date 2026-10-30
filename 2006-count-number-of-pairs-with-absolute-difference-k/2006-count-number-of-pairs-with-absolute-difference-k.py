class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        count=0
        dici={}
        for i in nums:
            if i not in dici:
                dici[i]=1
            else:
                dici[i]+=1
        for j in nums:
            ans=j+k
            if ans in dici:
                count+=dici[ans]
        return count
        