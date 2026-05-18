class MinStack:
    # two stacks solution, O(1) time for all ops, O(n) space
    # one stack stores the values, and the other stores the min at each level
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        curr_min = self.getMin()
        if curr_min == None or curr_min > val:
            curr_min = val
        self.min_stack.append(curr_min)

    # make sure the level of both stacks is consistent
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None
        
