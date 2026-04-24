class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        # A clear path requires both the start and end cells to be empty (0).
        # If either the top-left or bottom-right cell is blocked (1), no path exists.
        if grid[0][0] or grid[N-1][N-1]:
            return -1

        q = deque([(0,0,1)])
        visit = set((0,0))
        # 8-directional moves from (r, c)

        # Horizontal/Vertical moves
        direct = [
            (0, 1),   # right
            (1, 0),   # down
            (0, -1),  # left
            (-1, 0),  # up

            # Diagonal moves
            (1, 1),    # bottom-right
            (-1, 1),   # top-right
            (1, -1),   # bottom-left
            (-1, -1)   # top-left
        ]

        while q:
            r,c, length = q.popleft()
            # If we've reached the destination (bottom-right), return the path length
            # 'length' counts the number of cells visited along this path.
            if r == N-1 and c == N -1:
                return length

            for dr, dc in direct:
                nr, nc = r + dr, c + dc
                if (0<= nr < N and 0 <= nc < N and grid[nr][nc] == 0 and 
                    (nr,nc) not in visit):
                    q.append((nr,nc, length + 1))
                    visit.add((nr, nc))
        return -1

        