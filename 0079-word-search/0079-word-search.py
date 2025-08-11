class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(row, col, length):
            if length == len(word):
                return True
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False
            if board[row][col] != word[length]:
                return False

            length += 1
            temp = board[row][col] 
            board[row][col] = "#"
            found = (
                dfs(row - 1, col, length)
                or dfs(row + 1, col, length)
                or dfs(row, col - 1, length)
                or dfs(row, col + 1, length)
            )
            board[row][col] = temp

            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False

# Time: O(M × N × 4^L) where L = len(word), because each step has at most 4 directions.

# Space: O(L) recursion depth.