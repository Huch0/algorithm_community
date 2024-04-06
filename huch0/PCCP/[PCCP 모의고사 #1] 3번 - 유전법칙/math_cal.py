def solution(queries):
    answer = []

    for n, p in queries:
        answer.append(gene(n, p))

    return answer


def gene(n, p):
    index = p
    indices = []

    for _ in range(n - 1):
        index = (p - 1) % 4
        indices.append(index)
        p = (p - 1) // 4 + 1

    cur_node = "Rr"
    for i in range(n - 2, -1, -1):
        if cur_node == "RR" or cur_node == "rr":
            return cur_node

        index = indices[i]
        children = ["RR", "Rr", "Rr", "rr"]
        cur_node = children[index]

    return cur_node
