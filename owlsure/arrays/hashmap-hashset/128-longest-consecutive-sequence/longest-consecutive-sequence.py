class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        longest_seq = 0
        for num in seq:
            if num-1 not in seq:
                curr_num = num
                curr_streak = 1
                while(curr_num+1 in seq):
                    curr_num+=1
                    curr_streak+=1
                longest_seq = max(longest_seq, curr_streak)
        return longest_seq