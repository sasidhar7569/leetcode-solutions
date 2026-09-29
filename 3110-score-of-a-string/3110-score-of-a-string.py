class Solution:
    def scoreOfString(self, s: str) -> int:
        result=0
        n=len(s)
        for i in range(1,n):
            result+=abs(ord(s[i-1])-ord(s[i]))
        return result

        