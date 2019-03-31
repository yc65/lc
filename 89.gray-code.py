#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#
# https://leetcode.com/problems/gray-code/description/
#
# algorithms
# Medium (45.09%)
# Total Accepted:    129.3K
# Total Submissions: 285.9K
# Testcase Example:  '2'
#
# The gray code is a binary numeral system where two successive values differ
# in only one bit.
# 
# Given a non-negative integer n representing the total number of bits in the
# code, print the sequence of gray code. A gray code sequence must begin with
# 0.
# 
# Example 1:
# 
# 
# Input: 2
# Output: [0,1,3,2]
# Explanation:
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
# 
# For a given n, a gray code sequence may not be uniquely defined.
# For example, [0,2,3,1] is also a valid gray code sequence.
# 
# 00 - 0
# 10 - 2
# 11 - 3
# 01 - 1
# 
# 
# Example 2:
# 
# 
# Input: 0
# Output: [0]
# Explanation: We define the gray code sequence to begin with 0.
# A gray code sequence of n has size = 2^n, which for n = 0 the size is 2^0 =
# 1.
# Therefore, for n = 0 the gray code sequence is [0].
# 
# 
#
class Solution:
    # n=1: [0, 1]; n=2: loop [0, 1] forward and add "0" for each; 
    # then loop [0, 1] backward and add "1" for each; for n=3,  
    # loop the res of n=2 forward and add "0" for each, loop the
    # the res of n=1 bacward and add "1" for each
    def grayCode(self, n: int) -> List[int]:
        if not n: return [0]
        arr = [0, 1]
        len_arr = 2
        for i in range(2, n+1):
            # print(len_arr)
            for j in range(len_arr-1, -1, -1):
                arr.append(arr[j] | 1<<(i-1))
            len_arr<<=1
        return arr



