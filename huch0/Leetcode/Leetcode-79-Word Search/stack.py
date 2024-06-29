class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        if len(word) > m * n:
            return False

        # For large cases
        counter = collections.defaultdict(int)
        starts = []
        cnt_starts = []
        for i in range(m):
            for j in range(n):
                counter[board[i][j]] += 1

                if board[i][j] == word[0]:
                    starts.append((i, j))
                if board[i][j] == word[-1]:
                    cnt_starts.append((i, j))

        if not starts or not cnt_starts:
            return False

        if len(word) == 1:
            return True

        # Choose starts set with smaller one
        if len(starts) > len(cnt_starts):
            word = word[::-1]
            starts = cnt_starts

        # Check is the whole word in board
        for char in word:
            if counter[char] == 0:
                return False
            counter[char] -= 1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        stack = [(1, [start]) for start in starts]
        while stack:
            i, path = stack.pop()
            x, y = path[-1]

            if i > len(word):
                continue

            for dx, dy in directions:
                nx, ny = dx + x, dy + y

                if (nx, ny) in path or nx < 0 or m <= nx or ny < 0 or n <= ny:
                    continue

                if board[nx][ny] == word[i]:
                    if i == len(word) - 1:
                        # print(i, nx, ny)
                        return True

                    stack.append((i + 1, path + [(nx, ny)]))

        return False
