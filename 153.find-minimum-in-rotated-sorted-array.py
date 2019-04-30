#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
class Solution:
    def findMin(self, nums: List[int]) -> int:
        self.res = float('inf')
        def rec(l, r):
            if l > r: return
            if nums[l]<=nums[r]:
                self.res = min(self.res, nums[l])
                # print(self.res)
            else:
                mid = (l+r+1)//2
                rec(l, mid-1)
                rec(mid, r)
        rec(0, len(nums)-1)
        return self.res
