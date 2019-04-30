#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#
class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        s += ' '
        temp = ''
        for c in s:
            if c == ' ':
                if temp:
                    res.insert(0, temp)
                    temp = ''
            else:
                temp+=c
        return ' '.join(res)

