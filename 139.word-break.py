#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
class Solution:
    # dp (1-D)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s: return False
        len_s = len(s)
        dp = [False] * (len_s+1)
        dp[0] = True
        # i refers to the idx in dp; if within [0:i], s[0:j] is matchable and s[j:i]
        # is matchable, then [0:i] is matchable
        for i in range(1, len_s+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]

