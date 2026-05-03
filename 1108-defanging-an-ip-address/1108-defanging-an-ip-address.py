class Solution:
    def defangIPaddr(self, address: str) -> str:
        version=""
        for ch in address:
            version=address.replace(".","[.]")
        return version        

