class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        #approach: sliding window + hashmap
        """ 
        sliding window: left/right pointers define substring
        hashmap: count[char] tracks frequency of each letter
        track maxCount: highest frequency of any character 
            valid window: window length-maxCount <= k; otherwise shrink from left
        """
        left = 0
        max_count = 0
        count ={}
        max_length = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0)+1
            max_count = max(max_count, count[s[right]])

            while (right-left+1) - max_count > k:
                count[s[left]]-=1
                left+=1
            max_length = max(max_length, right-left+1)
        return max_length

        