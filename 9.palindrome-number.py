#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (42.02%)
# Total Accepted:    519.4K
# Total Submissions: 1.2M
# Testcase Example:  '121'
#
# Determine whether an integer is a palindrome. An integer is a palindrome when
# it reads the same backward as forward.
# 
# Example 1:
# 
# 
# Input: 121
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
# 
# 
# Example 3:
# 
# 
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# 
# 
# Follow up:
# 
# Coud you solve it without converting the integer to a string?
# 
#
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x!=0 and x%10==0):
            return False
        rev_x = 0
        while x>rev_x: # note how end condition is set: 
                       # we may get x==12, x_rev=123 for 12321 or x==1, x_rec== 1 for 11
            rev_x = rev_x * 10 + int(x%10)
            x = int(x/10)
        return x in (int(rev_x/10), rev_x)

# test cases
# 10000
# -121
# 1304834
# 184841
# 13531
# 11
