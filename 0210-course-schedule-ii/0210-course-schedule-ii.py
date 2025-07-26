class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree=[0]*n
        prereq_map = defaultdict(list)

        for course, prereq in prerequisites:
            indegree[course]+=1
            prereq_map[prereq].append(course)

        queue=deque()
        for i in range(n):
            if indegree[i]==0:
                queue.append(i)

        ans=[]
        while queue:
            prereq = queue.popleft()
            ans.append(prereq)

            for nei in prereq_map[prereq]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    queue.append(nei)

        return ans if len(ans)==n else []
        
# Time Complexity: O(V+E) where V represents the number of vertices and E represents the number of edges. We pop each node exactly once from the zero in-degree queue and that gives us V. Also, for each vertex, we iterate over its adjacency list and in totality, we iterate over all the edges in the graph which gives us E. Hence, O(V+E)

# Space Complexity: O(V+E). The in-degree array requires O(V) space. We use an intermediate queue data structure to keep all the nodes with 0 in-degree. In the worst case, there won't be any prerequisite relationship and the queue will contain all the vertices initially since all of them will have 0 in-degree. That gives us O(V). Additionally, we also use the adjacency list to represent our graph initially. The space occupied is defined by the number of edges because for each node as the key, we have all its adjacent nodes in the form of a list as the value. Hence, O(E). So, the overall space complexity is O(V+E).