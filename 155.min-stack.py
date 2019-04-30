#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # the stack stores both the elements and the current min element
        self.stack = [(None, float('inf'))]

    def push(self, x: int) -> None:
        return self.stack.append((x, min(self.stack[-1][1], x)))

    def pop(self) -> None:
        if len(self.stack)>1:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

