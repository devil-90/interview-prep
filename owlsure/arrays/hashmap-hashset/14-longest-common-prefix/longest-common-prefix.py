class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: #["flower","flow","flight"]

        res = ""
        for i in range(len(strs[0])): # i=0 to 5
            for s in strs[1:]:   #flower
                if len(s)== i or strs[0][i] != s[i]: 
                    return res
            res+=strs[0][i]
        return res

        