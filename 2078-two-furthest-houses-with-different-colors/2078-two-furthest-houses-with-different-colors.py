class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans=0
        k=len(colors)
        for i in range(k):
           
            if colors[i]!=colors[0]:
                ans=max(ans,i)
            if colors[i]!=colors[k-1]:
                x=abs(i-(k-1))
                ans=max(ans,x)    

        
                        
        return  ans          