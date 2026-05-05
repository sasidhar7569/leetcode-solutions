class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans=0
        k=len(colors)
        for i in range(k):
            if colors[i]!=colors[k-1]:
                x=abs((i-(k-1)))
                ans=max(ans,x)
        for j in range(k-1,0,-1):
            if colors[j]!=colors[0]:
                x=abs(j)
                ans=max(ans,x)

                        
        return  ans          