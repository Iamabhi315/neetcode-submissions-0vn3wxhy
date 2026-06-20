class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dit = {
            '[' : ']',
            '{' : '}',
            '(' : ')'
        }
        for c in s:
            if c == '[' or c == '{' or c == '(':
                stack.append(c)
            else:
                if not stack:
                    return False
                elif c == dit[stack[-1]]:
                    stack.pop()
                else:
                    return False

        return not stack