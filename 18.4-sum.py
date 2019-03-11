#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (29.74%)
# Total Accepted:    214.8K
# Total Submissions: 720.9K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers and an integer target, are there elements
# a, b, c, and d in nums such that a + b + c + d = target? Find all unique
# quadruplets in the array which gives the sum of target.
# 
# Note:
# 
# The solution set must not contain duplicate quadruplets.
# 
# Example:
# 
# 
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
# 
# A solution set is:
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
# 
#
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        len_nums = len(nums)
        i=0
        while i < len_nums-3:
            j = i+1
            while j < len_nums-2:
                m, n = j+1, len_nums-1
                while m < n:
                    temp = nums[i] + nums[j] + nums[m] + nums[n]
                    if temp == target:
                        res.append([nums[i], nums[j], nums[m], nums[n]])
                        m+=1
                        n-=1
                        # Note: don't forget the m<n condition
                        while m<n and nums[m] == nums[m-1]:
                            m+=1
                        while m<n and nums[n] == nums[n+1]:
                            n-=1
                    elif temp < target:
                        m+=1
                    else:
                        n-=1
                j+=1
                # Note don't forget the j<len_nums-2 condition
                while j > i+1 and j<len_nums-2 and nums[j]== nums[j-1]:
                    j+=1
            i+=1
            # Note don't forget the i<len_nums-3 condition
            while i>0 and i<len_nums-3 and nums[i] == nums[i-1]:
                i+=1
        return res
                        


