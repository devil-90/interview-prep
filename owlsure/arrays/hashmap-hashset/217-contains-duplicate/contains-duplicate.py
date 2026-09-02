class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in range(len(nums)):
            if nums[num] in seen:
                return True
            seen[nums[num]] = 1 
        return False