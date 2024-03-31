class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_cnt = Counter(tasks)
        task_info = [[task_cnt[t], -(n + 1)] for t in task_cnt]
        task_info.sort(key=lambda x: -x[0])
        run_tasks = 0
        # print(task_info)

        cycle = 0
        while run_tasks < len(tasks):
            for i, t in enumerate(task_info):
                if t[0] == 0:
                    task_info.pop(i)
                elif cycle - t[1] > n:
                    t[1] = cycle  # last execution cycle
                    t[0] -= 1  # remain tasks

                    j = i + 1
                    while j < len(task_info) and task_info[j][0] > t[0]:
                        j += 1
                    task_info[i], task_info[j -
                                            1] = task_info[j - 1], task_info[i]

                    run_tasks += 1
                    break

            # print(cycle, task_info)
            cycle += 1

        return cycle
