class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dici={}
        for ch in stones:
            if ch in dici:
                dici[ch]+=1
            else:
                dici[ch]=1
        ans=0        
        for j in jewels:
            if j in dici:
                ans=ans+dici[j]
        return ans 
        # ans=0
        # for ch in stones:
        #     if ch in jewels:
        #         ans+=1
        # return ans           

