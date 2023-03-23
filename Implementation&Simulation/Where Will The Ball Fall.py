class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        res = []
        if len(grid[0]) == 1:
            res.append(-1)
            return res
        print(len(grid[0]))
        for c in range(0, len(grid[0])):
            col = c
            resulting = 0
            for r in range(0, len(grid)):
                if grid[r][col] == 1 and col+1 <= len(grid[0])-1:
                    if grid[r][col+1] == grid[r][col]:
                        col += 1
                    else:
                        resulting = -1
                        break
                elif grid[r][col] == -1 and col-1 >= 0:
                    if grid[r][col-1] == grid[r][col]:
                        col -= 1
                    else:
                        resulting = -1
                        break
                elif grid[r][col] == 1 and col+1 == len(grid[0]):
                    resulting = -1
                    break
                elif grid[r][col] == -1 and col-1 == -1:
                    resulting = -1
                    break
            if resulting == -1:
                resutling = -1
            else:
                resulting = col
            res.append(resulting)
        return res