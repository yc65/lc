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
    # def threeSum(self, nums):
        res = []
        len_nums = len(nums)
        s_before_i = set()
        for i in range(0, len_nums-2):
            s = {}
            target = 0-nums[i]
            for j in range(i+1, len_nums):
                if target-nums[j] in s and s[target-nums[j]] == True:
                    if i == 0:
                        res.append([nums[i], nums[j], target-nums[j]])
                        # the following two lines avoid duplicates in the two_sum
                        s[target-nums[j]] = False
                        s[nums[j]] = False
                    # the follwing elif avoid appending nums[j] which has the same as previous nums[i]
                    elif nums[j] not in s_before_i and nums[i] not in s_before_i and target-nums[j] not in s_before_i:
                        res.append([nums[i], nums[j], target-nums[j]])
                        # the following two lines avoid duplicates in the two_sum
                        s[target-nums[j]] = False
                        s[nums[j]]=False
                else:
                    # the following if clause avoid duplicates in the two_sum
                    if nums[j] not in s:
                        s[nums[j]] = True
            s_before_i.add(nums[i])     
        return res

# if __name__ == "__main__":
#     slt = Solution()
#     slt.threeSum([-1, 0, 1, 2, -1, -4])
            