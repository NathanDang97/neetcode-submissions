class MinStack:
    # one stack solution, O(1) time for all ops, O(n) space
    # the idea is to append a tutple rather than one value to the stack
    # each tuple contains the value and the minimum at the time the value is added
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        curr_min = self.getMin()
        if curr_min == None or curr_min > val:
            curr_min = val
        self.stack.append((val, curr_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None
        
    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None
        
