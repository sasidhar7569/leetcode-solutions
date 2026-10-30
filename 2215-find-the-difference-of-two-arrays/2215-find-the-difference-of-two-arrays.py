class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        a=set(nums1)
        b=set(nums2)
        c=list(a-b)
        d=list(b-a)
        return [c,d]
        