#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (23.44%)
# Total Accepted:    492K
# Total Submissions: 2.1M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
# 
# Note:
# 
# The solution set must not contain duplicate triplets.
# 
# Example:
# 
# 
# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        s = set()
        len_nums = len(nums)
        nums.sort()
        # print(nums)
        for i in range(0, len_nums-2):
            j = i+1
            k = len_nums-1
            while j<k:
                next_one = True
                if i > 0 and nums[i] == nums[i-1]:break
                if j > i+1 and nums[j] == nums[j-1] or nums[j] in s:
                    j += 1
                    next_one = False
                if k+1<len_nums and nums[k] == nums[k+1] or nums[k] in s:
                    k -= 1
                    next_one = False
                if next_one:
                    temp = nums[i] + nums[j] + nums[k] 
                    if temp == 0:
                        res.append([nums[i], nums[j], nums[k]])
                        j+=1
                        k-=1
                    elif temp < 0:
                        j+=1
                    else:
                        k-=1
            s.add(nums[i])
        return res
