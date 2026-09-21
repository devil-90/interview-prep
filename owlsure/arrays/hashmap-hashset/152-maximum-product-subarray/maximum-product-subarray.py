class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        left=1
        right=1
        ans=nums[0]
        n=len(nums)-1
        for i in range(len(nums)):
            left = left or 1
            right = right or 1

            left*=nums[i]
            right*=  nums[n-i]     
            ans = max(left, right, ans)
        return ans