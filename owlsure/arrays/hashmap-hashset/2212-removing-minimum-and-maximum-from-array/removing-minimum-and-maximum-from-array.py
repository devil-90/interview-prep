class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        
        left_idx = min(min_idx, max_idx)
        right_idx = max(min_idx, max_idx)

        from_front = right_idx + 1
        from_back = n - left_idx
        from_both = (left_idx + 1) + (n - right_idx)

        return min(from_front, from_back, from_both)

