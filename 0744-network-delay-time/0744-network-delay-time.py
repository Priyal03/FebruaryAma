class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # create adjList
        adjList=defaultdict(list)
        
        for src,dest,w in times:
            adjList[src].append((dest,w))

        minHeap=[(0,k)] # time, node
        visited = set()
        ans=0

        while minHeap:

            time, node = heapq.heappop(minHeap)
            if node in visited:
                continue

            ans = max(ans, time)
            visited.add(node)
            
            if len(visited)==n:
                return ans

            for destNode, destWeight in adjList[node]:

                if destNode not in visited:
                    heapq.heappush(minHeap, (time+destWeight, destNode))
        
        return -1

# Time: O(E log N) —

# Each edge is pushed at most once into the heap.

# Heap operations are log N.

# Space: O(N + E) for graph, heap, visited.