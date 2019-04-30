#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
class Solution:
    # stack
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = None
        operators = ["+", "-", "*", "/"]
        for tk in tokens:
            if tk in operators:
                curr1 = stack.pop()
                curr2 = stack.pop()
                # NOTE: push the current result back to stack
                if tk == "+":
                    stack.append(curr2 + curr1)
                elif tk == "-":
                    stack.append(curr2 - curr1)
                elif tk == "*":
                    stack.append(curr2 * curr1)
                elif tk == "/":
                    stack.append(int(curr2 / curr1))
            else:
                stack.append(int(tk))
        return stack[-1]


