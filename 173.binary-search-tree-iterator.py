#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # 在遍历过程中，如果某个节点存在右儿子，则继续从右儿子开始push入栈直到其最左节点
    # result = 3, 6
    # 因为6有右儿子，所以6被pop出去之后，从6为root开始push入栈直到最左节点，然后stack为：
     def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        curr = self.stack.pop()
        node = curr.right
        while node:
            self.stack.append(node)
            node = node.left
        return curr.val
        
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return True if self.stack else False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

