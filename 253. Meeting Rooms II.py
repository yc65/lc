#Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

#Example 1:

#Input: [[0, 30],[5, 10],[15, 20]]
#Output: 2
#Example 2:

#Input: [[7,10],[2,4]]
#Output: 1
#NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

class Solution:
    # heap
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        import heapq
        # Sort the meetings in increasing order of their start time.
        intervals.sort()
        rooms = []
        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(rooms, intervals[0][1])
        for itv in intervals[1:]:
            # If the room due to free up the earliest is free, assign that room to this meeting.
            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            if rooms[0] > itv[0]:
                heapq.heappush(rooms,itv[1])
            else:
                heapq.heappop(rooms)
                heapq.heappush(rooms,itv[1])
            # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(rooms)

