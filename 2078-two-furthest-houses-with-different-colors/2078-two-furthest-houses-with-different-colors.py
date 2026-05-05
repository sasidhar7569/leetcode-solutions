class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans=0
        for i in range(1,len(colors)):
            for j in range(i,len(colors)):
                if colors[i-1]!=colors[j]:
                    x=abs((i-1)-j)
                    ans=max(ans,x)
        return ans            