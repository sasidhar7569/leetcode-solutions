class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dici={}
        r={}
        iso=True
        for i in range(len(s)):
            x=s[i]
            y=t[i]
            if x not in dici and y not in r:
                dici[x]=y
                r[y]=x
            elif x in dici and dici[x]!=y:
                iso=False
                break
            elif y in r and r[y]!=x:
                iso=False
                break    
        return iso            



