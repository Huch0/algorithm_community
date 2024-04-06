def solution(queries):
    answer = []

    for n, p in queries:
        answer.append(gene(n, p))

    return answer


def gene(n, p):
    if n == 1:
        return "Rr"

    parent = gene(n - 1, (p - 1) // 4 + 1)

    index = (p - 1) % 4
    if parent == "Rr":
        if index == 0:
            return "RR"

        if index == 3:
            return "rr"

    return parent
