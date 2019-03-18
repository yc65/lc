#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (44.81%)
# Total Accepted:    304.5K
# Total Submissions: 674.4K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
# 
# Example:
# 
# 
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# Note:
# 
# 
# All inputs will be in lowercase.
# The order of your output does not matter.
# 
# 
#
class Solution:
    # sort string
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            b = ''.join(sorted(i))
            if b in res:
                res[b] += [i]
            else:
                res[b] = [i]
        return [res[i] for i in res]

