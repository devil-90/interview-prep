class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for num in range(len(nums)):
            difference = target - nums[num]
            if difference in seen:
                return [seen[difference], num]
            seen[nums[num]] = num