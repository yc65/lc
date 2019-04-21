#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#
# https://leetcode.com/problems/word-ladder-ii/description/
#
# algorithms
# Hard (17.15%)
# Total Accepted:    115.5K
# Total Submissions: 664.7K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# all shortest transformation sequence(s) from beginWord to endWord, such
# that:
# 
# 
# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
# 
# 
# Note:
# 
# 
# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# 
# 
# Example 1:
# 
# 
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# Output:
# [
# ⁠ ["hit","hot","dot","dog","cog"],
# ["hit","hot","lot","log","cog"]
# ]
# 
# 
# Example 2:
# 
# 
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# Output: []
# 
# Explanation: The endWord "cog" is not in wordList, therefore no possible
# transformation.
# 
# 
# 
# 
# 
#
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        from collections import defaultdict
        # step 1: get all possible candidates
        all_combinations = defaultdict(list)
        len_w = len(beginWord)
        for w in wordList:
            for i in range(len_w):
                all_combinations[w[:i]+"*"+w[i+1:]].append(w)
        
        # step 2: bfs to get the graph
        dfs_path = defaultdict(set)
        queue = [beginWord]
        visited = set([beginWord])
        while queue:
            len_curr_level = len(queue)
            seen_curr_level = set() # NOTE: use visited to record nodes that have seen in the previous
                                    # levels; and seen_curr_level to record nodes that have been seen
                                    # in the current level. Since two parent nodes may point to the same 
                                    # child node, if we recorded as visited when we see this child for one
                                    # of the parent, the this child won't be processed again when processing
                                    # the other parent
            for x in range(len_curr_level):
                curr_w = queue.pop(0)
                for i in range(len_w):
                    intermediate = curr_w[:i]+'*'+curr_w[i+1:]
                    if intermediate in all_combinations:
                        for next_w in all_combinations[intermediate]:
                            if next_w not in visited:
                                seen_curr_level.add(next_w)
                                dfs_path[curr_w].add(next_w)
                                queue.append(next_w)
            visited |= seen_curr_level
        # print (dfs_path)

        # step 3: dfs to construct the paths
        res = []
        dfs_visited = {}

        def construct_path(prev_path, word):
            dfs_visited[word] = True
            if word == endWord:
                res.append(prev_path+[word])
            else:
                if word in dfs_path:
                    for child in dfs_path[word]:
                        if child not in dfs_visited or dfs_visited[child] == False:
                            construct_path(prev_path+[word], child)
            dfs_visited[word] = False 
        construct_path([], beginWord)
        return res
