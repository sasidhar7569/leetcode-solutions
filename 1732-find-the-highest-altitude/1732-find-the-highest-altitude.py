class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        ans=0
        temp=0
        for i in gain:
            temp+=i
            ans=max(ans,temp)
        return ans
        