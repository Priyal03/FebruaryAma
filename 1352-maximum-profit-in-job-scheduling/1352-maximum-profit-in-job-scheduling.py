class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}
        n = len(intervals)

        def dfs(i):

            if i == n:
                return 0
            if i in cache:
                return cache[i]

            # find jth index where startTime is just greater or == than current endTime
            j = bisect.bisect_right(intervals, (intervals[i][1],0,0)) # The -1, -1 ensures that if a job starts exactly at end_time, we don’t accidentally skip it.

            take_profit = intervals[i][2] + dfs(j) # now you have reached non-overlapping interval with index j.

            skip_profit = dfs(i + 1)  # skip this index, move to next possibility
            
            cache[i] =  max(skip_profit, take_profit)

            return cache[i]

        return dfs(0)

# Time: O(N log N) (sorting + binary search per job).  and, Space: O(N).