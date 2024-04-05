def solution(ability):
    m = len(ability)
    n = len(ability[0])
    sorted_ab = []

    for sp in range(n):
        sp_ab = [(st, ability[st][sp]) for st in range(m)]
        sp_ab.sort(key=lambda x: x[1], reverse=True)
        sorted_ab.append(sp_ab[:n])

    max_sum, cur_sum = 0, 0
    cur_studs = []

    def dfs(idx):
        nonlocal max_sum, cur_sum

        if idx == n:
            max_sum = max(max_sum, cur_sum)
            return

        n_recur = 0
        for st, ab in sorted_ab[idx][:n]:
            if st not in cur_studs:
                cur_studs.append(st)
                cur_sum += ab
                dfs(idx + 1)
                cur_studs.pop()
                cur_sum -= ab

                n_recur += 1

            if n_recur == n - idx:
                return

    dfs(0)

    return max_sum
