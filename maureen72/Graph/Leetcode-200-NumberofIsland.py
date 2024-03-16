class Solution:
    def numIslands(self, grid: List[List[str]])-> int:
        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands += 1
                    stack = [(i, j)]

                    while len(stack) > 0:
                        x, y = stack.pop()

                        # Mark x,y as visited
                        grid[x][y] = '0'

                        adjs = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

                        for adj in adjs:
                            ax, ay = adj
                            if 0 <= ax < len(grid) and 0 <= ay <len(grid[0]) and grid[ax][ay] == '1':
                                stack.append((ax, ay))

        return islands