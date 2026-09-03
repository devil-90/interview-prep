class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for char in magazine:
            d[char]=d.get(char, 0)+1

        for char in ransomNote:
            if char not in d:
                return False
            d[char]-=1
            if d[char]<0:
                return False
        return True
        