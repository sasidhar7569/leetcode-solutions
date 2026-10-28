class Solution:
    def firstUniqChar(self, s: str) -> int:
        k=-1
        for i in range(len(s)):
            target=s[i]
            for j in range(len(s)):
                if i!=j and s[j]==target:
                    break
            else:
                k=i
                break
        return k
        