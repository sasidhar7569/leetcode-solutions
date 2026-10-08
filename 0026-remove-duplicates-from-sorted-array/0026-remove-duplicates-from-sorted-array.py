class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow=0
        for fast in range(len(nums)):
            if nums[fast] not in nums[0:fast]:
                nums[slow]=nums[fast]
                slow+=1
        return slow       