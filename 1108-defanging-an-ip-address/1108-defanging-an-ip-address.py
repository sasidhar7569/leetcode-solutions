class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans=""
        
        ans=address.replace(".","[.]")
        return ans
        