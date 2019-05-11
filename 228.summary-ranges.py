#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# Given a sorted integer array without duplicates, return the summary of its ranges.

# Example 1:

# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
# Example 2:

# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums: return res
        start = 0
        len_nums = len(nums)
        for i in range(1,len_nums):
            if nums[i]-nums[i-1]>1:
                if start == i-1:
                    res.append(str(nums[i-1]))
                else:
                    res.append(str(nums[start]) + "->" + str(nums[i-1]))
                start = i
            else:
                continue
        if start == len_nums-1:
            res.append(str(nums[start]))
        else:
            res.append(str(nums[start]) + "->" + str(nums[len_nums-1]))
        return res        

