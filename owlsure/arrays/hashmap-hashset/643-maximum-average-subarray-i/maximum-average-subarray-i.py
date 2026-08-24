class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_of_window = sum(nums[:k])
        ans = (sum_of_window)
        for i in range(k, len(nums)):
           sum_of_window = (sum_of_window - nums[i-k] + nums[i])
           ans = max(sum_of_window, ans)
        return ans/k