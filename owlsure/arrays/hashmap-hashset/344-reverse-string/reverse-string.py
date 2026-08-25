class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        j = len(s)-1
        for char in range(len(s)//2):
            temp = s[char]
            s[char] = s[j]
            s[j] = temp
            j-=1
            
        