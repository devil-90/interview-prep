class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1, rob2 = 0, 0
        for num in nums:
            curr_max = max(rob1+num, rob2)
            rob1 = rob2
            rob2 = curr_max
        return rob2


        # def rob_rec(index):
        #     if index>=len(nums):
        #         return 0
        #     # robbing current house and moving to index+2
        #     take = nums[index] + rob_rec(index+2)
        #     # not robbing and moving to next house
        #     skip = rob_rec(index+1)
        #     return max(take, skip)
        # return rob_rec(0)
        