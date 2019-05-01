#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#
class Solution:
    # binary search
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r+1)//2
            # print("mid ", mid)
            # if mid is larger that mid-1, it means peak is on the right part of mid
            if nums[mid] > nums[mid-1]:
                l = mid
            else:
                r = mid-1
        return l
        
