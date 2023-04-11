class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:    
        
        q = deque()
        time, fresh = 0, 0
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append([i,j])

        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    rx, cx = r + dr, c + dc
                    if (rx in range(rows) and
                        cx in range(cols) and
                        grid[rx][cx] == 1): 
                        grid[rx][cx] = 2
                        q.append([rx,cx])
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1