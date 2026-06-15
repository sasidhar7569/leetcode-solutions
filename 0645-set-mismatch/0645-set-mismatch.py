class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s=set()
        first=0
        second=0
        k=len(nums)
        for i in range(k):
            if nums[i] not in s:
                s.add(nums[i])
            else:
                first+=nums[i]
        for j in range(1,k+1):
            if j in s:
                continue
            else:
                second+=j
        return [first,second]                        

        # dici={}
        # for j in nums:
        #     if j not in dici:
        #         dici[j]=1
        #     else:
        #         dici[j]+=1
        # for j in dici:
        #     if dici[j]==2:
        #         s.append(j)        
        # for i in range(1,k+1):
        #     if i in dici:
        #         continue
        #     else:
        #         s.append(i)        
                  
        
        return s          
        