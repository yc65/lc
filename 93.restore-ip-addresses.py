#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#
# https://leetcode.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (30.86%)
# Total Accepted:    133.4K
# Total Submissions: 430.8K
# Testcase Example:  '"25525511135"'
#
# Given a string containing only digits, restore it by returning all possible
# valid IP address combinations.
# 
# Example:
# 
# 
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]
# 
# 
#
class Solution:
    # backtracking
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 16:
            return []
        res = []
        def backtracking(ss, idx, path):
            # idx stores how many subparts we have
            if idx == 4:
                if not ss: 
                    # if we've already got four subparts, and there's no numbers left
                    # then we got a valid ip address
                    res.append(path[:-1])
                    return
            for i in range(1, 4):
                if i <= len(ss):
                    if i == 1:
                        # pick out one digit as a subpart
                        backtracking(ss[i:], idx+1, path+ss[:i]+".")
                    elif i == 2 and ss[0] != '0':
                        # pick out two digits as a subpart
                        backtracking(ss[i:], idx+1, path+ss[:i]+".")
                    elif i == 3 and ss[0] != '0' and int(ss[:3]) <=255:
                        # pick out three digits as a subpart
                        backtracking(ss[i:], idx+1, path+ss[:i]+".")
        backtracking(s, 0, '')
        return res

