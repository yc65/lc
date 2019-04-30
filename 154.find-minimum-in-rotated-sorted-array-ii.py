#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#
class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums)-1
        while i <= j:
            while i < j and nums[i] == nums[i+1]:
                i+=1
            # print("i ",i)
            while i < j and nums[j] == nums[j-1]:
                j-=1
            # print("j ",j)
            if i == j: return nums[i]
            if nums[i] < nums[j]: return nums[i]
            mid = (i+j+1)//2
            # print("mid ", mid)
            if nums[mid] < nums[mid-1]: 
                return nums[mid]
            elif nums[mid] > nums[mid+1]:
                return nums[mid+1]

            if nums[mid] < nums[i]:
                j = mid-1
            elif nums[mid] > nums[j]:
                i = mid+1
            else:
                return nums[i]
            
            


