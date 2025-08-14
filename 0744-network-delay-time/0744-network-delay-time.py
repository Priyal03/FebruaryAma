#Dijkstra’s Algorithm
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adjList = defaultdict(list)
        for src, dest, w in times:
            adjList[src].append((dest, w))

        short_dist = {node: float("inf") for node in range(1, n + 1)}
        short_dist[k] = 0

        minHeap = [(0, k)]  # time, node
        while minHeap:

            time, node = heapq.heappop(minHeap)
            if time > short_dist[node]:
                continue

            for destNode, edgeWeight in adjList[node]:

                if time + edgeWeight < short_dist[destNode]:
                    short_dist[destNode] = time + edgeWeight
                    heapq.heappush(minHeap, (short_dist[destNode], destNode))

        max_dist = max(short_dist.values())
        return max_dist if max_dist != float("inf") else -1


# Time: O(E log N)
# Each edge is pushed at most once into the heap.

# Heap operations are log N.
# Space: O(N + E) for graph, heap, visited.
