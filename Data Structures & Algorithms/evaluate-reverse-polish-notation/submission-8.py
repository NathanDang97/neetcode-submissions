class Solution:
    # solution using stack, O(n) time and space
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]
        stack = []

        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                if t == "+":
                    stack.append(n2 + n1)
                elif t == "-":
                    stack.append(n2 - n1)
                elif t == "*":
                    stack.append(n2 * n1)
                else:
                    stack.append(int(n2 / n1))

        return stack[-1]