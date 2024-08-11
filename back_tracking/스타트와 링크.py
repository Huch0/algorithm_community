from itertools import combinations

def calculate_team_score(team, s):
    score = 0
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            score += s[team[i]][team[j]] + s[team[j]][team[i]]
    return score

def find_min_difference(n, s):
    players = list(range(n))
    min_difference = float('inf')

    for start_team in combinations(players, n // 2):
        link_team = [player for player in players if player not in start_team]
        
        start_score = calculate_team_score(start_team, s)
        link_score = calculate_team_score(link_team, s)
        
        difference = abs(start_score - link_score)
        min_difference = min(min_difference, difference)

    return min_difference

def main():
    import sys
    input = sys.stdin.readline

    n = int(input().strip())
    s = [list(map(int, input().strip().split())) for _ in range(n)]

    result = find_min_difference(n, s)
    print(result)

if __name__ == "__main__":
    main()