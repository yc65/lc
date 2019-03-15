#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (30.05%)
# Total Accepted:    217.9K
# Total Submissions: 724.1K
# Testcase Example:  '[1,2,3]'
#
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
# 
# If such arrangement is not possible, it must rearrange it as the lowest
# possible order (ie, sorted in ascending order).
# 
# The replacement must be in-place and use only constant extra memory.
# 
# Here are some examples. Inputs are in the left-hand column and its
# corresponding outputs are in the right-hand column.
# 
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
#
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # pernumtation explaination: [[1,2,3],[1,3,2][2,1,3][2,3,1][3,1,2][3,2,1]]
        len_nums = len(nums)
        if len_nums == 0 or len_nums == 1: return
        # find the i where nums[i] < nums[i+1]; if all nums[i] > nums[i+1], then i = -1
        i = len_nums-1
        while i >= 0:
            if nums[i-1] < nums[i]:
                i-=1
                break
            i -= 1
        # within nums[i+1:], find the smallest number which is larger than nums[i], swap this with i
        if i >= 0:
            k = i + 1
            while nums[k]>nums[i]:
                k+=1
                if k == len_nums:
                    break
            nums[i], nums[k-1] = nums[k-1], nums[i]
        # reverse nums[i+1:]
        j = len_nums-1
        i += 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j-=1

