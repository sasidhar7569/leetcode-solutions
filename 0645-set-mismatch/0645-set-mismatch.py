class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s=[]
        k=len(nums)
        dici={}
        for j in nums:
            if j not in dici:
                dici[j]=1
            else:
                dici[j]+=1
        for j in dici:
            if dici[j]==2:
                s.append(j)        
        for i in range(1,k+1):
            if i in dici:
                continue
            else:
                s.append(i)        
                  
        
        return s 
        