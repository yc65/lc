#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
class Solution:
    # dp
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        # res = float("-inf")
        res = min_val = max_val = nums[0]
        for n in nums[1:]:
            # when multiplied by a negative number, the minvalue becomes the maxvalue
            # and the maxvalue becomes the minvalue
            if n < 0:
                min_val, max_val = max_val, min_val
            min_val = min(n, min_val*n)
            max_val = max(n, max_val*n)
            res = max(max_val, res)
        return res
