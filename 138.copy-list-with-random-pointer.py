#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        curr = head
        # hash table of original node to copy node
        # if original node alreay has a copy, return copy
        # so that we don't create it again.
        visited = {}
        new_head = None
        while curr:
            if curr not in visited:
                new_node = Node(curr.val, None, None)
                visited[curr] = new_node
                if curr == head: new_head = new_node
            else:
                new_node = visited[curr]
            
            if curr.next:
                if curr.next not in visited:
                    new_next = Node(curr.next.val, None, None)
                    visited[curr.next] = new_next
                else:
                    new_next = visited[curr.next]
                new_node.next = new_next
            
            if curr.random:
                if curr.random not in visited:
                    new_random = Node(curr.random.val, None, None)
                    visited[curr.random] = new_random
                else:
                    new_random = visited[curr.random]
                new_node.random = new_random

            curr = curr.next

        return new_head
