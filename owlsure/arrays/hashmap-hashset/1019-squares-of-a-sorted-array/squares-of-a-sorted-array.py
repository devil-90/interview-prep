class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        low = 0
        high = n-1
        res = [0] * n 
        i=n-1
        while(low<=high):
            left_square = nums[low]**2
            right_square = nums[high]**2
            if(left_square>right_square):
                res[i] = left_square
                low+=1
            else:
                res[i] = right_square
                high-=1
            i-=1
        return res 

        