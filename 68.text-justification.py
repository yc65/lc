#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#
# https://leetcode.com/problems/text-justification/description/
#
# algorithms
# Hard (22.63%)
# Total Accepted:    91.7K
# Total Submissions: 404.1K
# Testcase Example:  '["This", "is", "an", "example", "of", "text", "justification."]\n16'
#
# Given an array of words and a width maxWidth, format the text such that each
# line has exactly maxWidth characters and is fully (left and right)
# justified.
# 
# You should pack your words in a greedy approach; that is, pack as many words
# as you can in each line. Pad extra spaces ' ' when necessary so that each
# line has exactly maxWidth characters.
# 
# Extra spaces between words should be distributed as evenly as possible. If
# the number of spaces on a line do not divide evenly between words, the empty
# slots on the left will be assigned more spaces than the slots on the right.
# 
# For the last line of text, it should be left justified and no extra space is
# inserted between words.
# 
# Note:
# 
# 
# A word is defined as a character sequence consisting of non-space characters
# only.
# Each word's length is guaranteed to be greater than 0 and not exceed
# maxWidth.
# The input array words contains at least one word.
# 
# 
# Example 1:
# 
# 
# Input:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# Output:
# [
# "This    is    an",
# "example  of text",
# "justification.  "
# ]
# 
# 
# Example 2:
# 
# 
# Input:
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# Output:
# [
# "What   must   be",
# "acknowledgment  ",
# "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall
# be",
# because the last line must be left-justified instead of fully-justified.
# ⁠            Note that the second line is also left-justified becase it
# contains only one word.
# 
# 
# Example 3:
# 
# 
# Input:
# words =
# ["Science","is","what","we","understand","well","enough","to","explain",
# "to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
# Output:
# [
# "Science  is  what we",
# ⁠ "understand      well",
# "enough to explain to",
# "a  computer.  Art is",
# "everything  else  we",
# "do                  "
# ]
# 
# 
#
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        if not words: return []
        res = []
        n = maxWidth
        sub_str = []
        # len_words = len(words)
        for w in  words:
            len_w = len(w)
            if n == len_w:
                sub_str.append(w)
                res.append(' '.join(sub_str))
                n = maxWidth
                sub_str = []
            elif n > len_w:
                sub_str.append(w)
                n -= (len_w+1)
            else:
                n+=1 # the last word should not be followed by a space
                # print(n)
                if len(sub_str) == 1:
                    res.append(sub_str[0] + ' '* (n))
                else:
                    div, mod = divmod(n, len(sub_str)-1)
                    # print(div, mod, sub_str)
                    if mod == 0:
                        res.append((' '*(div+1)).join(sub_str))
                    else:
                        temp = ''
                        len_sub_str = len(sub_str)
                        for idx, s in enumerate(sub_str):
                            temp += s
                            if idx != len_sub_str-1:
                                if idx < mod:
                                    temp += ' '*(div+2)
                                else:
                                    temp += ' '*(div+1)
                        res.append(temp)
                sub_str = []
                n = maxWidth
                sub_str.append(w)
                n -= (len_w+1)
        if sub_str:
            res.append(' '.join(sub_str)+' '*(n+1)) 

        return res
       