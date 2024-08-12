class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    answer = answer + 1
                    self.delIsland(grid, row, col)
        return answer

    def delIsland(self, map, row, col): # 재귀 함수로써, 해당 육지와 연결되는 모든 곳을 없앤다 - 
        map[row][col] = '0'
        m, n = len(map), len(map[0])
        if row-1 > -1 and map[row-1][col] == '1':
            self.delIsland(map, row-1, col)
        if col-1 > -1 and map[row][col-1] == '1':
            self.delIsland(map, row, col-1)
        if row+1 < m and map[row+1][col] == '1':
            self.delIsland(map, row+1, col)
        if col+1 < n and map[row][col+1] == '1':
            self.delIsland(map, row, col+1)