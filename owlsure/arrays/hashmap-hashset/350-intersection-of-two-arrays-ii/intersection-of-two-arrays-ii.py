class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        unique = set()
        freq1 = {}
        freq2 = {}
        ans = []
        for num in nums1:
            freq1[num] = freq1.get(num,0)+1
            unique.add(num)
        for num in nums2:
            if num in unique:
                freq2[num] = freq2.get(num,0)+1
                
        
        for num in unique:
            if num in freq2:
                value = min(freq1[num], freq2[num])
                while value!=0:
                    ans.append(num)
                    value-=1
        return ans

        
        