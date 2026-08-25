class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for num in range(1, len(nums)):
            if nums[num] != nums[j]:
                j+=1
                nums[j] = nums[num]
                

        return j+1