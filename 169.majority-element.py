#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
class Solution:
    # Boyer-Moore
    # Essentially, what Boyer-Moore does is look for a suffix 
    # sufsufsuf of nums where suf[0]suf[0]suf[0] is the majority 
    # element in that suffix. To do this, we maintain a count, 
    # which is incremented whenever we see an instance of our 
    # current candidate for majority element and decremented 
    # whenever we see anything else.
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for n in nums:
            if count == 0:
                candidate = n
            if candidate == n:
                count += 1
            else:
                count -= 1
        return candidate


