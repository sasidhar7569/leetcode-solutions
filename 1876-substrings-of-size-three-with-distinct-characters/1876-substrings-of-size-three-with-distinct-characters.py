class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l=0
        k=3
        temp=""
        count=0
        for r in range(len(s)):
            temp+=s[r]
            if(r-l==k):
                temp=temp.replace(s[l],"",1)
                l+=1
            if(r-l+1==k):
                if s[l]!=s[l+1] and s[l]!=s[r] and s[l+1]!=s[r]:
                    count+=1
        return count
        