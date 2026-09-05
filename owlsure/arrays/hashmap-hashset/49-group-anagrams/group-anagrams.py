class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for word in strs:
            hashcode = [0]*26
            for char in word:
                code = ord(char)-ord("a")
                hashcode[code]+=1
            ans[tuple(hashcode)].append(word)
        
        return list(ans.values())