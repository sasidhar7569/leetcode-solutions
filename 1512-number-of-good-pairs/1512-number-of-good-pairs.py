class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dici={}
        for i in nums:
            if i in dici:
                dici[i]+=1
            else:
                dici[i]=1
        ans=0
        for j in dici:
            a=dici[j] 
            b=(a*(a-1))/2
            ans=ans+b
        return int(ans)                
        # count=0
        # n=len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i]==nums[j]:
        #             count+=1
        # return count            

        