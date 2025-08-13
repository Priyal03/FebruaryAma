# When we encounter an ending event, that means that some meeting that started earlier has ended now. We are not really concerned with which meeting has ended. All we need is that some meeting ended thus making a room available.
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        s=e=0
        result=count=0

        while s<len(intervals):
            if start[s]<end[e]:
                count+=1
                s+=1
                result=max(result,count)
            else:
                count-=1
                e+=1
            
        return result

# Time: O(N log N) — sorting only.

# Space: O(N) — for start/end array