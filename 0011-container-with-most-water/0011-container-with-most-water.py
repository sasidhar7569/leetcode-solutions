class Solution:
    def maxArea(self, height: list[int]) -> int:
        left=0
        right=len(height)-1
        ans=0
        while left<right:
            if height[left]>=height[right]:
                r=(right-left)*height[right]
                right-=1

            else:
                r=(right-left)*height[left]
                left+=1

            ans=max(ans,r)
            
        return ans
            
        