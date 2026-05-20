class Solution:
    # solution using stack, O(n) time and space
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesis_map = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            else:
                if not stack:
                    return False
                curr_open = stack.pop()
                if curr_open != parenthesis_map[c]:
                    return False

        return False if stack else True