class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # The number of islands
        islands = 0

        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                # Find a land
                if grid[i][j] == '1':
                    islands += 1
                    stack = [(i, j)]

                    while len(stack) > 0:
                        x, y = stack.pop()

                        # Mark x,y as visited
                        grid[x][y] = '0'

                        adjacents = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

                        for adj in adjacents:
                            ax, ay = adj
                            # Check adjacent vertex is within grid range
                            # and the land('1')
                            if 0 <= ax < m and 0 <= ay < n and grid[ax][ay] == '1':
                                stack.append((ax, ay))

        return islands