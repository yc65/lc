#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (23.16%)
# Total Accepted:    124.7K
# Total Submissions: 536.9K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# You are given a string, s, and a list of words, words, that are all of the
# same length. Find all starting indices of substring(s) in s that is a
# concatenation of each word in words exactly once and without any intervening
# characters.
# 
# Example 1:
# 
# 
# Input:
# ⁠ s = "barfoothefoobarman",
# ⁠ words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar"
# respectively.
# The output order does not matter, returning [9,0] is fine too.
# 
# 
# Example 2:
# 
# 
# Input:
# ⁠ s = "wordgoodgoodgoodbestword",
# ⁠ words = ["word","good","best","word"]
# Output: []
# 
# 
#
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        len_s = len(s)
        w_num = len(words)
        if len_s==0 or w_num == 0: return [] # don't forget corner cases
        len_w = len(words[0])
        i = 0
        res = []
        while i < len_s-len_w+1:
            remain_words = w_num
            h = Counter(words)
            matched = False
            temp = i
            while remain_words:
                w = s[i:i+len_w]
                word_count = h.get(w)
                if word_count:
                    h[w]-= 1
                    remain_words -= 1
                    i += len_w
                    matched = True
                else:
                    matched = False
                    break
            if matched:
                res.append(temp)
            if temp + w_num * len_w >= len_s: break # break early to save time
            i = temp+1 # notice how to update i
        return res

