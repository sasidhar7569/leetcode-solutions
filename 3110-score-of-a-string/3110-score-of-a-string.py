class Solution:
    def scoreOfString(self, s: str) -> int:
        score=0
        me=[]
        for ch in s:
            me.append(ord(ch))
        for i in range(1,len(me)):
            k=abs((me[i-1])-(me[i]))

            score=k+score
        return score    