class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums)<3:
            return []
        #sorting 
        nums.sort()
        if nums[0]>0:
            return []
        res = []
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            low = i+1
            high = len(nums)-1
            sum = 0
            while low<high:
                sum = nums[i]+nums[low]+nums[high]
                if sum>0:
                    high-=1
                elif sum<0:
                    low+=1
                else:
                    res.append([nums[i], nums[low], nums[high]])
                    last_low_occurence = nums[low]
                    last_high_occurence = nums[high]
                    while low<high and nums[low] == last_low_occurence:
                        low+=1
                    while low<high and nums[high] == last_high_occurence:
                        high-=1
        return res
            
        