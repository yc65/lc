#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        if m > 0:
            n = len(grid[0])
        else:
            return 0
        
        def dfs(i, j):
            # print(i, j)
            # NOTE: don't forget when i, j are invalid
            if i >= m or j >= n or i < 0 or j < 0: 
                return
            if grid[i][j] == "0":
                return
            else:
                grid[i][j] = "0"
                # NOTE: look at all of the four directions
                dfs(i+1, j)
                dfs(i, j+1)
                dfs(i-1, j)
                dfs(i, j-1)
        res = 0
        for id_i in range(m):
            for id_j in range(n):
                if grid[id_i][id_j] == "1":
                    dfs(id_i, id_j)
                    # print(grid)
                    res += 1
        return res
        

