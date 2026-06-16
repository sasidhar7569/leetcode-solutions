class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dici={}
        ans=False
        for i in nums:
            if i in dici:
                ans=True
                break
            dici[i]=1
        return ans    
        # ans=True
        # for i in nums:
        #     if i not in dici:
        #         dici[i]=1
        #     else:
        #         dici[i]+=1
        # for j in dici:
        #     if dici[j]>=2:
        #         ans=True
        #         break
        #     else:
        #         ans=False   
        # return ans                  
        