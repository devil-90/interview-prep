class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [0]*(len(encoded)+1)
        res[0] = first
        for i in range(len(encoded)):
            res[i+1] = encoded[i] ^ res[i]
        return res