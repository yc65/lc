#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#
class Solution:
    # math
    def convertToTitle(self, n: int) -> str:
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        res = ""
        while n > 0:
            remainder = n % 26
            res = capitals[remainder-1] + res
            # NOTE how to update n!!
            n = (n-1) // 26
        # res += capitals[n-1] + res
        return res
