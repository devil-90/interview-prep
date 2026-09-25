class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        freq_count = {}
        for char in t:
            freq_count[char] = freq_count.get(char,0)+1
        
        required = len(freq_count)
        left,right = 0,0

        window_count = {}
        formed = 0
        ans = float("inf"), None, None
        
        while right<len(s):
            char = s[right]
            window_count[char] = window_count.get(char,0)+1

            if char in freq_count and window_count[char] == freq_count[char]:
                formed+=1
            while left <= right and formed == required:
                char = s[left]
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                window_count[char] -=1
                if char in freq_count and window_count[char] < freq_count[char]:
                    formed -= 1
                left+=1
            right+=1
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]



        
        