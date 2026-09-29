class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans=""
        for i in address:
            ans=address.replace(".","[.]")
        return ans
        