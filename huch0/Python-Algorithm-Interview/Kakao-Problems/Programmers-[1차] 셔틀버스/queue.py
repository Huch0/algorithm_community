import heapq
import collections


def solution(n, t, m, timetable):
    def HHMMtoM(HHMM):
        HH, MM = HHMM.split(':')
        return int(HH) * 60 + int(MM)

    def MtoHHMM(M):
        h = M // 60
        m = M % 60
        return "%02d:%02d" % (h, m)

    heap = []
    heap_size = 0
    first_time = HHMMtoM("09:00")
    last_time = first_time + t * (n - 1)
    queue_table = collections.defaultdict(list)

    for x in timetable:
        mx = HHMMtoM(x)
        heapq.heappush(heap, mx)

    while heap:
        mx = heapq.heappop(heap)
        index = max(0, (mx - 1 - first_time) // t + 1)

        while index < n:
            if len(queue_table[index]) < m:
                queue_table[index].append(mx)
                break
            index += 1

    if len(queue_table[n - 1]) > 0:
        if len(queue_table[n - 1]) == m:
            return MtoHHMM(queue_table[n - 1][-1] - 1)

    return MtoHHMM(last_time)
