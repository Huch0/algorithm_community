class Banker:
    def __init__(self, n: int, m: int, Available: list[int], Max: list[list[int]], Allocation: list[list[int]], Need: list[list[int]] = None):
        self.n = n
        self.m = m
        self.Available = Available
        self.Max = Max
        self.Allocation = Allocation
        if Need is None:
            self.Need = [[Max[i][j] - Allocation[i][j] for j in range(m)] for i in range(n)]
            print("Need: ", self.Need)
        else:
            self.Need = Need

    def get_safe_state_sequence(self, verbose=True) -> list[int]:
        Work = self.Available
        Finish = [False for _ in range(self.n)]
        if verbose:
            print("Work: ", Work, "Finish: ", Finish)
            print("{:<10} {:<20} {:<20} {:<30} {:<20}".format(
                "thread_i", "Need[i]", "Work", "Work + Allocation[i]", "Safe"))
        Safe = []
        for _ in range(self.n):
            for i in range(self.n):
                if Finish[i] == False:
                    if all(j >= 0 for j in [Work[k] - self.Need[i][k] for k in range(self.m)]):
                        if verbose:
                            print("{:<10} {:<20} {:<20}".format(i, str(self.Need[i]), str(Work)), end="")
                        Work = [Work[k] + self.Allocation[i][k] for k in range(self.m)]
                        Finish[i] = True
                        Safe.append(i)
                        if verbose:
                            print("{:<30} {:<20}".format(str(Work), str(Safe)))
                        break
        if all(Finish):
            return Safe

        if verbose:
            print("Unsafe state")
        return None

    def request(self, i: int, Request_i: list[int], verbose=True) -> bool:
        if not all(Request_i[j] <= self.Need[i][j] for j in range(self.m)):
            print("Error: Request_i > Need_i")
            return False

        if not all(Request_i[j] <= self.Available[j] for j in range(self.m)):
            print("Thread must wait : Request_i > Available")
            return False

        if verbose:
            print("Thread", i, "requests", Request_i)
            print("{:<20} {:<20} {:<20} {:<20}".format("", "Available", "Allocation[i]", "Need[i]"))
            print("{:<20} {:<20} {:<20} {:<20}".format(
                "Before Requset", str(self.Available), str(self.Allocation[i]), str(self.Need[i])))

        # Allocate requested resources to thread i and update Available, Allocation, Need
        self.Available = [self.Available[j] - Request_i[j] for j in range(self.m)]
        self.Allocation[i] = [self.Allocation[i][j] + Request_i[j] for j in range(self.m)]
        self.Need[i] = [self.Need[i][j] - Request_i[j] for j in range(self.m)]

        if verbose:
            print("{:<20} {:<20} {:<20} {:<20}".format(
                "After Request", str(self.Available), str(self.Allocation[i]), str(self.Need[i])))

        if self.get_safe_state_sequence(verbose=False) is None:
            # Rollback
            self.Available = [self.Available[j] + Request_i[j] for j in range(self.m)]
            self.Allocation[i] = [self.Allocation[i][j] - Request_i[j] for j in range(self.m)]
            self.Need[i] = [self.Need[i][j] + Request_i[j] for j in range(self.m)]

            if verbose:
                print("Thread must wait : Request is not safe")
            return False

        return True


if __name__ == "__main__":

    params = [
        {
            'n': 5,
            'm': 3,
            'Available': [3, 3, 2],
            'Max': [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]],
            'Allocation': [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]],
            'Need': [[7, 4, 3], [1, 2, 2], [6, 0, 0], [0, 1, 1], [4, 3, 1]]
        },
        {
            'n': 5,
            'm': 4,
            'Available': [1, 5, 2, 0],
            'Max': [[0, 0, 1, 2], [1, 7, 5, 0], [2, 3, 5, 6], [0, 6, 5, 2], [0, 6, 5, 6]],
            'Allocation': [[0, 0, 1, 2], [1, 0, 0, 0], [1, 3, 5, 4], [0, 6, 3, 2], [0, 0, 1, 4]],
            'Need': [[0, 0, 0, 0], [0, 7, 5, 0], [1, 0, 0, 2], [0, 0, 2, 0], [0, 6, 4, 2]]
        },
        {
            'n': 5,
            'm': 4,
            'Available': [0, 3, 0, 1],
            'Max': [[5, 1, 1, 7], [3, 2, 1, 1], [3, 3, 2, 1], [4, 6, 1, 2], [6, 3, 2, 5]],
            'Allocation': [[3, 0, 1, 4], [2, 2, 1, 0], [3, 1, 2, 1], [0, 5, 1, 0], [4, 2, 1, 2,]],
            'Need': None
        },
        {
            'n': 5,
            'm': 4,
            'Available': [1, 0, 0, 2],
            'Max': [[5, 1, 1, 7], [3, 2, 1, 1], [3, 3, 2, 1], [4, 6, 1, 2], [6, 3, 2, 5]],
            'Allocation': [[3, 0, 1, 4], [2, 2, 1, 0], [3, 1, 2, 1], [0, 5, 1, 0], [4, 2, 1, 2,]],
            'Need': None
        }
    ]

    # ex1 = Banker(**params[1])
    # print(ex1.get_safe_state_sequence())
    # print(ex1.request(1, [0, 4, 2, 0]))
    # ex2 = Banker(**params[2])
    # print(ex2.get_safe_state_sequence())
    ex3 = Banker(**params[3])
    print(ex3.get_safe_state_sequence())
