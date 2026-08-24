class Solution:
    def maxArea(self, height: List[int]) -> int:
        low=0
        high=len(height)-1
        ans = 0
        while(low<high):
            amount = (high-low)*min(height[low], height[high])
            ans = max(ans, amount)
            if(height[low]<height[high]):
                low+=1
            else:
                high-=1
        return ans