class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = (re.sub(r'[^A-Za-z0-9]',"",s)).lower()
        n = len(text)-1
        for i in range(len(text)//2):
            if text[i] == text[n-i]:
                continue
            return False
        
        return True