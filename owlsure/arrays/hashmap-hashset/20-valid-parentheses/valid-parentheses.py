class Solution:
    def isValid(self, s: str) -> bool:

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
                top = stack[-1]
                if top == braces[brace]:
                    stack.pop(len(stack)-1)
                else:
                    return False
        return len(stack) == 0