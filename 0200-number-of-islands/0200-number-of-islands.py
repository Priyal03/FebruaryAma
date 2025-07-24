# Instead of recursion, use a queue to explore neighbors.
# Useful if you want to avoid stack overflow on large grids.
# python recursion depth is 1000 calls, java = 10k calls  or 1 MB stack space.
# O(m*n) both
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # if not grid:
        #     return 0

        total = 0
        rows = len(grid)
        cols = len(grid[0])

        def bfs(row,col):
            
            queue=deque()
            queue.append((row,col))
            grid[row][col]='0'

            while queue:
                r,c = queue.popleft()
                for dr, dc in [(-1,0),(0,-1),(1,0),(0,1)]:
                    nr = dr+r
                    nc=c+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]=='1':
                        grid[nr][nc]='0'
                        queue.append((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1':
                    bfs(r,c)
                    total+=1

        return total 