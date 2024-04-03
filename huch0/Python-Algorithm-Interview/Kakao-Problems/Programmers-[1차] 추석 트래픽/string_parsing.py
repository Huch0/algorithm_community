def solution(lines):
    criterion = []
    for line in lines:
        s, f = line_to_start_finish(line)
        criterion.append((s, 1))
        criterion.append((f, -1))

    criterion.sort(key=lambda x: x[0])

    accum = 0
    max_req = 1
    for i, e1 in enumerate(criterion):
        cur = accum

        for e2 in criterion[i:]:
            if e2[0] - e1[0] > 999:
                break
            if e2[1] > 0:
                cur += e2[1]

        max_req = max(max_req, cur)
        accum += e1[1]

    return max_req


def line_to_start_finish(line):
    log = line.split(" ")
    finish_time = S_to_ms(log[1])
    duration = T_to_ms(log[2])
    start_time = finish_time - duration + 1

    return (start_time, finish_time)


def S_to_ms(S):
    ts = S.split(':')

    hh = int(ts[0]) * 60 * 60
    mm = int(ts[1]) * 60

    ss_sss = ts[2].split('.')
    ss = int(ss_sss[0])

    return (hh + mm + ss) * 1000 + int(ss_sss[1])


def T_to_ms(T):
    T = float(T[:-1])
    return int(T * 1000)


def test():
    print(S_to_ms("01:00:04.002"))
    print(T_to_ms("2s"))
    print(T_to_ms("2.3s"))
    print(T_to_ms("2.34s"))

# test()
