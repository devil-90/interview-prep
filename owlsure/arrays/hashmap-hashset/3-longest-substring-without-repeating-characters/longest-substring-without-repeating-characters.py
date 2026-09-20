class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        length = 0
        left = 0
        for right in range(len(s)):
            curr = 0
            if s[right] in seen:
                while s[right] in seen:
                    
                    seen.remove(s[left])
                    left+=1
            seen.add(s[right])
            curr=right-left+1
            length= max(length, curr)

        return length

        