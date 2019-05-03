#
# @lc app=leetcode id=164 lang=python3
#
# [164] Maximum Gap
#



# class Bucket:
#     def __init__(self):
#         self.isUsed = False
#         self.minVal = float("inf")
#         self.maxVal = -float("inf")

# class Solution:
#     def maximumGap(self, nums: List[int]) -> int:
#         n = len(nums)
        
#         if n < 2:
#             return 0
#         minNum = min(nums)
#         maxNum = max(nums)

#         bucketSize = max(1, (maxNum - minNum) // (n - 1))
#         bucketNum = (maxNum - minNum) // bucketSize + 1
        
#         buckets = [Bucket() for _ in range(bucketNum)]
        
#         for num in nums:
#             bucketIdx = (num - minNum) // bucketSize
#             buckets[bucketIdx].isUsed = True
#             buckets[bucketIdx].minVal = min(buckets[bucketIdx].minVal, num)
#             buckets[bucketIdx].maxVal = max(buckets[bucketIdx].maxVal, num)
#         print([(bucket.maxVal, bucket.minVal) for bucket in buckets])
#         res = 0
#         prevEnd = None
#         for bucket in buckets:
#             if not bucket.isUsed: continue
                
#             if prevEnd != None:
#                 res = max(res, bucket.minVal - prevEnd)
#             prevEnd = bucket.maxVal
        
#         return res

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if not nums: return 0
        max_val = max(nums)
        min_val = min(nums)
        if max_val == min_val: return 0
        k = (max_val - min_val) // (len(set(nums))-1)
        bucket_num = (max_val - min_val) // k + 1
        buckets = {i:[float('inf'), float('-inf')] for i in range(bucket_num)}

        for n in nums:
            bucket_id = (n - min_val)//k
            buckets[bucket_id][0] = max(buckets[bucket_id][0], n) if buckets[bucket_id][0] != float('inf') else n
            buckets[bucket_id][1] = min(buckets[bucket_id][1], n) if buckets[bucket_id][1] != float('-inf') else n
        # print (buckets)
        start = buckets[0][0]
        res = 0
        for idx, values in buckets.items():
            if idx > 0:
                if (values[0] == float("inf") and values[1] == float("-inf")):
                    continue
                else:
                    res = max(res, values[1]-start) # min - prev_max
                    start = values[0]                    
        
        return res



