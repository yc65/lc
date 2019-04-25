#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#
class Solution:
    # bit manipulation
    def singleNumber(self, nums: List[int]) -> int:
        one, two = 0, 0
        for n in nums:
            one, two, three = one ^ n, two | (one & n), two & n
            one, two = one & ~three, two & ~three
        return one



