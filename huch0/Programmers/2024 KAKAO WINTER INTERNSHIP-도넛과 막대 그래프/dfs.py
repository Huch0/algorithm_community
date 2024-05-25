from collections import defaultdict


def solution(edges):
    v_created = 0
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    childrens = defaultdict(list)

    for u, v in edges:
        in_degree[v] += 1
        out_degree[u] += 1
        childrens[u].append(v)

    # Find the v_created that has at least 2 out degree and 0 in degree
    for v in out_degree:
        if out_degree[v] >= 2 and in_degree[v] == 0:
            v_created = v
            break

    # Find the start vertices for each graphs
    graph_starts = childrens[v_created]
    n_donuts, n_polls, n_eights = 0, 0, 0

    for root in graph_starts:
        g_type = dfs(root, childrens)
        if g_type == 0:
            n_donuts += 1
        elif g_type == 1:
            n_polls += 1
        else:
            n_eights += 1

    return [v_created, n_donuts, n_polls, n_eights]


def dfs(root, childrens):
    stack = [root]
    visited = set()
    visit_counter = 0

    while stack:
        cur = stack.pop()

        # If any vertex is visited twice, it is eight graph
        # No need to check the rest of the graph
        if cur in visited:
            visit_counter += 1
        if visit_counter == 2:
            break

        visited.add(cur)
        children = childrens[cur]

        if len(children) == 0:
            return 1  # poll
        elif len(children) > 1:
            return 2  # eight

        if children[0] == root:
            return 0  # dounut

        stack.append(children[0])

    return 2  # eight
