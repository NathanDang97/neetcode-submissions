# solution using two queues
# O(n) time for push, O(1) time for the rest
# O(n) space
class MyStack:

    def __init__(self):
        self.q1 = deque() # main queue, guarantees LIFO order
        self.q2 = deque() # aux queue

    def push(self, x: int) -> None:
        # first, append to q2, 
        # then move all elements from q1 to q2
        # this would put the most recent element at the front of q2
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        # swap q1 and q2 since q1 is the main queue
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()