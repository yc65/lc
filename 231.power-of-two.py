#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# Given an integer, write a function to determine if it is a power of two.

# Example 1:

# Input: 1
# Output: true 
# Explanation: 20 = 1
# Example 2:

# Input: 16
# Output: true
# Explanation: 24 = 16
# Example 3:

# Input: 218
# Output: false
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # don't forget zero and negative numbers
        if n <= 0: return False
        mod = 0
        while n>1:
            if n % 2 != 0:
                return False
            n //= 2
        return True
        

