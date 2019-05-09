#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#
class Solution:
    # math
    def trailingZeroes(self, n: int) -> int:
        # All trailing zeros are come from even_num x 5, 
        # we have more even_num than 5, so only count factor 5.
        res = 0
        while n:
            res += n // 5
            n //= 5
        return res

