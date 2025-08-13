class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        
        minheap=[]
        heapq.heappush(minheap, intervals[0][1])

        for start, end in (intervals[1:]):
            minEndTime = minheap[0]
            
            #remove whenever starttime is greater than minimum top element as meeting room can be available after that time.
            if start>=minEndTime:
                heapq.heappop(minheap)
            
            #keep pushing endTime in heap for every new intervals.    
            heapq.heappush(minheap, end)

        return len(minheap)

# Time: O(N log N) — sorting + heap push/pop.

# Space: O(N) for heap.
