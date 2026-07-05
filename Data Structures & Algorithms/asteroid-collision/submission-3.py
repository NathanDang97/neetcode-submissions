class Solution:
    # solution using a stack, O(n) time and space
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            # check for collision once a negative asteroid is encountered
            while stack and a < 0 and stack[-1] > 0:
                diff = stack[-1] + a
                # if the top asteroid in the stack is smaller in size, pop the stack
                if diff < 0:
                    stack.pop() 
                # if the top asteroid in the stack is bigger in size, ignore the current asteroid
                elif diff > 0:
                    a = 0
                # if the top asteroid and the current one are equal in size, both are destroyed
                else:
                    a = 0
                    stack.pop()

            # add an asteroid to the stack if the stack is empty
            # or if it's positive or if the stack of the top is negative
            if a != 0:
                stack.append(a)

        return stack