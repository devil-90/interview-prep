class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 !=0:
            return False
        stack = []
        braces = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for brace in s:
            if brace=="(" or brace=="[" or brace=="{":
                stack.append(brace)
            else:
                if not stack:
                    return False
                
                if stack[-1] == braces[brace]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0