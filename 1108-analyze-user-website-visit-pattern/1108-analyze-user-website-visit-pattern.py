from itertools import combinations
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        logs = sorted(zip(timestamp, username, website)) # sort logs by time

        userHistory=defaultdict(list) # build user to site mapping according to time
        for time, user, site in logs:
            userHistory[user].append(site)

        patternToUser=defaultdict(set) 
        for user, sites in userHistory.items():
            patterns = set(combinations(sites,3))# set of 3 sequences from user's visit History
            for p in patterns:
                patternToUser[p].add(user)

        max_count=0 # find the pattern with highest score (max user count)
        result=tuple()
        for pattern, users in patternToUser.items():
            if len(users)>max_count or (len(users)==max_count and pattern<result):
                result=pattern
                max_count=len(users)

        return list(result)

# | Metric | Value           |                            |
# | ------ | --------------- | -------------------------- |
# | Time   | O(n log n + n³) | (Sort + user combos)       |
# | Space  | O(n²)           | (Map of patterns to users) |
