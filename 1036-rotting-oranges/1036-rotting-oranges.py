class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        self.totalOranges=0
        self.minutes=0
        queue=deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    self.totalOranges+=1
                elif grid[r][c]==2:
                    queue.append((r,c))
            
        while queue and self.totalOranges>0:
            
            self.minutes+=1
            for i in range(len(queue)):

                r,c = queue.popleft()
                for dr, dc in [(-1,0),(0,-1),(1,0),(0,1)]:

                    nr = r+dr
                    nc = c + dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:

                        self.totalOranges-=1
                        grid[nr][nc]=2
                        queue.append((nr,nc))

        return -1 if self.totalOranges>0 else self.minutes

# Time Complexity: O(NM), where N×M is the size of the grid.

# First, we scan the grid to find the initial values for the queue, which would take O(NM) time.


# Then we run the BFS process on the queue, which in the worst case would enumerate all the cells in the grid once and only once. Therefore, it takes O(NM) time.


# Thus combining the above two steps, the overall time complexity would be O(NM)+O(NM)=O(NM)

# Space Complexity: O(NM), where N is the size of the grid.

# In the worst case, the grid is filled with rotten oranges. As a result, the queue would be initialized with all the cells in the grid.

# By the way, normally for BFS, the main space complexity lies in the process rather than the initialization. For instance, for a BFS traversal in a tree, at any given moment, the queue would hold no more than 2 levels of tree nodes. Therefore, the space complexity of BFS traversal in a tree would depend on the width of the input tree.