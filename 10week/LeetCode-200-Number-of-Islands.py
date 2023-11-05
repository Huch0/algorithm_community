class Solution:
    grid: list[list[str]]

    def dfs(self, i, j):
        # 더 이상 땅이 아닌 경우 종료
        if i < 0 or i >= len(self.grid) or \
            j < 0 or j >= len(self.grid[0]) or \
                self.grid[i][j] != '1':
            return
        
        self.grid[i][j] = 0
        
        # 동서남북 탐색
        self.dfs(i+1, j)
        self.dfs(i-1, j)
        self.dfs(i, j+1)
        self.dfs(i, j-1)

    def numIslands(self, grid: list[list[str]]) -> int:
        self.grid = grid
        # 예외 처리
        if not self.grid:
            return 0
        
        count = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                # 땅인 경우
                if self.grid[i][j] == '1':
                    self.dfs(i, j)
                    # 모든 육지 탐색 후 카운트 1 증가
                    count += 1
        
        return count