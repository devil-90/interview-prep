class Solution:
    def longestPalindrome(self, s: str) -> str:

        """
        approach: pick up any character from string and using two pointers move left and right to the character.
        """

        def check(i,j):
            left = i
            right = j-1
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True

        for i in range(len(s),0,-1):      
            for start in range(len(s)-i+1): 
                if check(start, start+i):    
                    return s[start: start+i]
        return ""

        