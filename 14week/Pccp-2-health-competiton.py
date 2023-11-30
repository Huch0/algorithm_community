### my first solution
answer = 0
max = 0

def solution(ability):
    m = len(ability)
    n = len(ability[0])

    def dfs(start, visited, score):
        x, y = start
        
        if ability[x][y] == 0:
            return

        global answer, max
        score += ability[x][y]

        if y == n-1:
            if score > max:
                max = score
                answer = score
            return
        
        for i in range(m):
            if i not in visited:
                visited.append(i)
                dfs((i, y+1), visited, score)
                visited.pop()
    
    for i in range(m):
        dfs((i, 0), [i], 0)
    
    return answer

# test case
# ability	result
# [[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]    210

#test code
if __name__ == '__main__':
    ability = [[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]
    answer = solution(ability)
    print(answer)