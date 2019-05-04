#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_list = version1.split('.')
        v2_list = version2.split('.')
        len_v1 = len(v1_list)
        len_v2 = len(v2_list)
        diff = abs(len_v1-len_v2)
        if len_v1 < len_v2:
            v1_list = v1_list+["0"]*diff
        else:
            v2_list = v2_list+["0"]*diff
        count = max(len_v1, len_v2)
        # print (v1_list, v2_list)
        for i in range(count):
            if int(v1_list[i])>int(v2_list[i]):
                return 1
            elif int(v1_list[i])<int(v2_list[i]):
                return -1
        return 0

