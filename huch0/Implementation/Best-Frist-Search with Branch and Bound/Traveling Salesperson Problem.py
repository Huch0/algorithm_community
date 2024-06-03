import heapq


def travel(n: int, W: list[list[int]]) -> tuple[list[int], int]:
    def length(path: list[int]) -> int:
        total = 0

        for i in range(len(path) - 1):
            total += W[path[i]][path[i + 1]]

        return total

    def bound(u: tuple[int, int, list[int]]) -> int:
        _, _, path = u
        print(path)
        # the length of the path so far
        lower_bound = length(path)

        visited = path[1:]
        for i in range(1, n + 1):
            if i == path[-1]:  # last vertex
                # can't go back to the vertices that have been visited and first vertex
                row_i = [W[i][j] for j in range(1, n + 1) if j not in visited and i != j and j != 1]
                if row_i:
                    lower_bound += min(row_i)
            elif i not in path[:-1]:  # not visited
                # can't go back to the vertices that have been visited
                row_i = [W[i][j] for j in range(1, n + 1) if j not in visited and i != j]
                if row_i:
                    lower_bound += min(row_i)
        print(lower_bound)
        return lower_bound

    v = (bound((0, 0, [1])), 0, [1])
    minlength = float("inf")
    opttour = []

    PQ = []
    heapq.heappush(PQ, v)

    while PQ:
        v = heapq.heappop(PQ)
        v_bound, v_level, v_path = v
        if v_bound < minlength:
            u_level = v_level + 1

            for i in range(2, n + 1):
                if i not in v_path:
                    # Put i at the end of the path
                    u_path = v_path + [i]  # Correctly create u_path as a new list

                    if u_level == n - 2:
                        # Put the vertex not in u.path at the end of u.path
                        for j in range(2, n + 1):
                            if j not in u_path:
                                u_path.append(j)
                                break
                        u_path.append(1)  # Make first vertex last one.

                        u = (bound((0, u_level, u_path)), u_level, u_path)

                        if length(u_path) < minlength:
                            minlength = length(u_path)
                            opttour = u_path
                    else:
                        u = (bound((0, u_level, u_path)), u_level, u_path)
                        if u[0] < minlength:
                            heapq.heappush(PQ, u)

    return opttour, minlength


if __name__ == "__main__":
    n = 5
    W = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 14, 4, 10, 20],
        [0, 14, 0, 7, 8, 7],
        [0, 4, 5, 0, 7, 16],
        [0, 11, 7, 9, 0, 2],
        [0, 18, 7, 17, 4, 0]
    ]

    print(travel(n, W))
