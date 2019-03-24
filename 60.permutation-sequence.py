#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#
# https://leetcode.com/problems/permutation-sequence/description/
#
# algorithms
# Medium (32.48%)
# Total Accepted:    131.6K
# Total Submissions: 404.7K
# Testcase Example:  '3\n3'
#
# The set [1,2,3,...,n] contains a total of n! unique permutations.
# 
# By listing and labeling all of the permutations in order, we get the
# following sequence for n = 3:
# 
# 
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 
# 
# Given n and k, return the k^th permutation sequence.
# 
# Note:
# 
# 
# Given n will be between 1 and 9 inclusive.
# Given k will be between 1 and n! inclusive.
# 
# 
# Example 1:
# 
# 
# Input: n = 3, k = 3
# Output: "213"
# 
# 
# Example 2:
# 
# 
# Input: n = 4, k = 9
# Output: "2314"
# 
# 
#
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n==1: return '1'
        res = ''
        i = 2
        mod = []
        numbers = [i for i in range(1, n+1)]
        m = 0
        while i <= n:
            if m == 0:
                k, m = k//i, k%i
            else:
                k, m = (k+1)//i, (k+1)%i
            mod.append(m)
            i += 1
        while mod:
            m = mod.pop()
            num = numbers.pop(m-1)
            res += str(num)
        res += str(numbers.pop())
        return res

