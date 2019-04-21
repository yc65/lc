#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#
# https://leetcode.com/problems/candy/description/
#
# algorithms
# Hard (27.88%)
# Total Accepted:    100.1K
# Total Submissions: 356.3K
# Testcase Example:  '[1,0,2]'
#
# There are N children standing in a line. Each child is assigned a rating
# value.
# 
# You are giving candies to these children subjected to the following
# requirements:
# 
# 
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# 
# 
# What is the minimum candies you must give?
# 
# Example 1:
# 
# 
# Input: [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1,
# 2 candies respectively.
# 
# 
# Example 2:
# 
# 
# Input: [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2,
# 1 candies respectively.
# ⁠            The third child gets 1 candy because it satisfies the above two
# conditions.
# 
# 
#
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings: return 0
        len_ratings = len(ratings)
        cache = [1 for i in range(len_ratings)]
        for i in range(1, len_ratings):
            if ratings[i]>ratings[i-1]:
                cache[i] = cache[i-1]+1
        # print(cache)
        res = cache[len_ratings-1]
        for i in range(len_ratings-2, -1, -1):
            if ratings[i+1] < ratings[i]:
                cache[i] = max(cache[i], cache[i+1]+1)
            res += cache[i]
        return res
