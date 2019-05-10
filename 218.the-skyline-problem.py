#
# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#


# A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

# Buildings  Skyline Contour
# The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

# For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

# The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

# For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

# Notes:

# The number of buildings in any input list is guaranteed to be in the range [0, 10000].
# The input list is already sorted in ascending order by the left x position Li.
# The output list must be sorted by the x position.
# There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]

class Solution:
    # divide and conquer 
    # (like merge sort)
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        n = len(buildings)
        if n == 0:
            return []
        if n == 1:
            print(buildings[0])
            x_start, y_end, height = buildings[0]
            print([[x_start, height], [y_end, 0]])
            return([[x_start, height], [y_end, 0]])
        # If there is more than one building, 
        # recursively divide the input into two subproblems.
        left_skyline = self.getSkyline(buildings[: n // 2])
        right_skyline = self.getSkyline(buildings[n // 2 :])
        
        # Merge the results of subproblem together.
        return self.merge_skylines(left_skyline, right_skyline)

    def merge_skylines(self,skl, skr):
        n_skl = len(skl)
        n_skr = len(skr)
        idl, idr = 0, 0
        curr_height, left_height, right_height = 0, 0, 0
        res = []
        while idl < n_skl and idr < n_skr:
            point_l, point_r = skl[idl], skr[idr]
            if point_l[0] < point_r[0]:
                x,left_height = point_l
                idl+=1
            else:
                x, right_height = point_r
                idr+=1
            max_height = max(left_height, right_height)
            if curr_height != max_height:
                if not res or res[-1][0] != x:
                    res.append([x, max_height])
                else:
                    res[-1][1] = max_height
                curr_height = max_height
        # print(res)   
        while idl < n_skl:
            x, y = skl[idl]
            if not res or res[-1][0] != x:
                res.append([x, y])
            else:
                res[-1][1] = y
            idl+=1
        # print(res)
        while idr < n_skr:
            x, y = skr[idr]
            if not res or res[-1][0] != x:
                res.append([x,y])
            else:
                res[-1][1] = y
            idr += 1
        # print(res)
        return res
            
              

