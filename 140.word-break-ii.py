#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#
class Solution:
    # backtracking -- this will exceed time limit
    # def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    #     if not s: return []
    #     self.res = []
    #     def backtracking(s, path):
    #         if not s:
    #             self.res.append(' '.join(path))
    #         else:
    #             len_s = len(s)
    #             for i in range(len_s+1):
    #                 if s[:i] in wordDict:
    #                     backtracking(s[i:], path+[s[:i]])
    #     backtracking(s, [])
    #     return self.res

    # dp with memoization
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    # def wordBreak(self, s, wordDict):   
        memo = {len(s): ['']}
        def sentences(i):
            if i not in memo:
                memo[i] = [s[i:j] + (tail and ' ' + tail)
                        for j in range(i+1, len(s)+1)
                        if s[i:j] in wordDict
                        for tail in sentences(j)]
            return memo[i]
        return sentences(0)


# if __name__ == "__main__":
#     sol = Solution()
#     sol.wordBreak("catsanddog",["cat", "cats", "and", "sand", "dog"])

