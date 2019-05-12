#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

# Example 1:

# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
class Solution:
    # time limit exceed...
    # def numSquares(self, n: int) -> int:
    #     cache = [0]*(n+1)
    #     base = 1
    #     for i in range(1, n+1):
    #         if i == base * base:
    #             cache[i] = 1
    #             base += 1
    #         else:
    #             # below is too slow, cannot pass
    #             # j = 1
    #             # mid = i // 2
    #             # min4i = float("inf")
    #             # while j <= mid:
    #             #     min4i = min(min4i, cache[j] + cache[i-j])
    #             #     j += 1
    #             # cache[i] = min4i
    #             min4i = float("inf")
    #             for b in range(1, base):
    #                 min4i = min(min4i, 1 + cache[i-b*b])
    #             cache[i] = min4i
    #     return cache[-1]
    
    # share dp among all test cases to save time
    _dp = [0]
    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]


