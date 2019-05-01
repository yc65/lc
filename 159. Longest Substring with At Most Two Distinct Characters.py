# Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

# Example 1:

# Input: "eceba"
# Output: 3
# Explanation: t is "ece" which its length is 3.

# Example 2:

# Input: "ccaabbb"
# Output: 5
# Explanation: t is "aabbb" which its length is 5.

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        m = {}
        len_m = 0
        len_s = len(s)
        fast, slow = 0, 0
        substr_len = 0
        while fast < len_s:
            if s[fast] in m:
                m[s[fast]] += 1
            else:
                m[s[fast]] = 1
                len_m += 1
            while len_m > 2 and slow < fast:
                m[s[slow]] -= 1
                if not m[s[slow]]:
                    del m[s[slow]]
                    len_m -= 1
                slow += 1
            substr_len = max(fast-slow+1, substr_len)
            fast+=1
        # print (m)
        return substr_len
             





