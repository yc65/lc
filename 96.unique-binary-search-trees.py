#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (45.35%)
# Total Accepted:    191.2K
# Total Submissions: 419.5K
# Testcase Example:  '3'
#
# Given n, how many structurally unique BST's (binary search trees) that store
# values 1 ... n?
# 
# Example:
# 
# 
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
# 
#
class Solution:
    # dp
    # catalan number: Cn+1 = sum(Ci*Cn-i for i <= n )
    # def numTrees(self, n: int) -> int:
    #     cache = [0]*(n+1)
    #     cache[0] = 1
    #     for i in range(1, n+1):
    #         for j in range(i):
    #             cache[i] += cache[j] * cache[i-1-j]
    #     return cache[n]

    # math: catalan number:
    # Cn = (2n)!/((n+1)!*n!)
    def numTrees(self, n: int) -> int:
        import math
        if n == 0:return 1
        return int(math.factorial(2*n)/(math.factorial(n+1)*math.factorial(n)))

