class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        substring = ""
        for i in range(len(s)):
            if(s[i] not in substring):
                substring = substring+s[i]
            else:
                while(s[i] in substring):
                    substring=substring[1:]
                substring=substring+s[i]
            ans = max(ans, len(substring))
        return ans