#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (35.04%)
# Total Accepted:    342.5K
# Total Submissions: 974.1K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
# 
# Note:
# 
# 
# The number of elements initialized in nums1 and nums2 are m and n
# respectively.
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2.
# 
# 
# Example:
# 
# 
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# Output: [1,2,2,3,5,6]
# 
# 
#
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = len(nums1)-1, n-1, m-1
        while j>= 0 and k >= 0:
            if nums2[j] >= nums1[k]:
                nums1[i] = nums2[j]
                i-=1
                j-=1
            else:
                nums1[i] = nums1[k]
                k-=1
                i-=1
        while j>=0:
            nums1[i] = nums2[j]
            i-=1
            j-=1
        
        

