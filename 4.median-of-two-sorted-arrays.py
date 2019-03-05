#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (25.57%)
# Total Accepted:    387.5K
# Total Submissions: 1.5M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
# 
# You may assume nums1 and nums2 cannot be both empty.
# 
# Example 1:
# 
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# 
# 
# Example 2:
# 
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5
# 
# 
#
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        # This condition is required to ensure that j is always between 0 to n and we'll never get Array Index out of bounds exception.
        # For Example: If i=0, and A is greater than B (i.e. m>n). j will become greater than n.??
        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1
        
        imin, imax, k = 0, m, int((m+n+1)/2) # kth element in nums1+nums2 is the median
                                             # median of n-length arry is (n+1)/2
        while (imin <= imax):
            i = int((imin+imax)/2)
            j = int((m+n+1)/2)-i

            if i>0 and nums1[i-1]>nums2[j]:
                # too many elements from nums1
                imax -= 1
            elif i < m and nums1[i] < nums2[j-1]:
                # too few elements from nums1
                imin+=1
            else:
                # we correctly separate nums1 and nums2 
                if i == 0:
                    max_of_left = nums2[j-1]
                elif j == 0:
                    max_of_left = nums1[i-1]
                else:
                    max_of_left = max(nums1[i-1], nums2[j-1])
                
                if (m+n)%2 != 0:
                    return max_of_left
                
                if i == m: # notice not m-1; so that [0:m-1] are all in the left
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                return (max_of_left+min_of_right)/2

