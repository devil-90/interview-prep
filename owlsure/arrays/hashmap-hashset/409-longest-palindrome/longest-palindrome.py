class Solution:
    def longestPalindrome(self, s: str) -> int:
        n = len(s)
        length = 0
        counts = Counter(s)
        has_odd = False
        
        for freq in counts.values():
            if freq%2 == 0:
                length+=freq
            else:
                length+= freq-1
                has_odd = True
        if has_odd:
            return length+1
        return length