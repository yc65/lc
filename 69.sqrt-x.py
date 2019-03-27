#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (30.84%)
# Total Accepted:    342.2K
# Total Submissions: 1.1M
# Testcase Example:  '4'
#
# Implement int sqrt(int x).
# 
# Compute and return the square root of x, where x is guaranteed to be a
# non-negative integer.
# 
# Since the return type is an integer, the decimal digits are truncated and
# only the integer part of the result is returned.
# 
# Example 1:
# 
# 
# Input: 4
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
# the decimal part is truncated, 2 is returned.
# 
# 
#
class Solution:
    # binary search 
    # NOTE the boundaries
    def mySqrt(self, x: int) -> int:
        i, j = 0, x//2+1
        while i <= j:
            # print(i, j)
            mid = i + (j-i)//2
            guess = mid ** 2
            # print(guess)
            if guess > x:
                j = mid-1
            elif guess == x:
                return mid
            else:
                i = mid+1
        return j

