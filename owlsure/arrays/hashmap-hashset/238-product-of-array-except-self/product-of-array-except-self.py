class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)-1
        prefix = [1]*(len(nums))
        suffix = [1]*len(nums)
        ans = []
        for i in range(n):
            prefix[i+1] = prefix[i] * nums[i]
            suffix[n-i-1] = suffix[n-i]*nums[n-i]
        for i in range(n+1):
            ans.append(prefix[i]*suffix[i])
        return ans

        