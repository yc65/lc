#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # NOTE: overlapping points both count
        from collections import defaultdict
        slope = defaultdict(set)
        len_points = len(points)
        if len_points == 0 or len_points == 1: return len_points
        res = 0
        for i in range(len_points-1):
            line = defaultdict(int)
            overlap = 1 # including the curr point itself
            curr_max = 0
            # get all the slopes passing i; find the slope with the maximum number of points
            for j in range(i+1, len_points):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                if dy == dx == 0:
                    overlap += 1
                    continue
                if dx == 0: # when the x-coordinate are the same
                    slope = None
                else:
                    slope = dy*10.0/dx # multiply 10.0 to get better precision for [[0,0],[94911151,94911150],[94911152,94911151]]

                line[slope] += 1
                curr_max = max(curr_max, line[slope])
            res = max(res, curr_max+overlap)

                # a = (points[i][1]-points[j][1])*1.0/(points[i][0]-points[j][0]) if (points[i][0]-points[j][0]) != 0 else 0
                # if (points[i][0]-points[j][0]) == 0: # NOTE: if x-coordinates are the same, y=b, a = 0, b = x-coordinate
                #     b = points[i][0]
                # else:
                #     b = points[i][1]-a*points[i][0]
                # # print(a, b)
                # slope[(a,b)].add(i)
                # slope[(a,b)].add(j)
        # print(slope)
        # res = max([len(v) for k, v in slope.items()])
        return res


