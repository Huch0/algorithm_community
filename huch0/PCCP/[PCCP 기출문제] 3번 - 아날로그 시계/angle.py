def solution(h1, m1, s1, h2, m2, s2):
    count = 0

    start_time = 3600 * h1 + 60 * m1 + s1
    end_time = 3600 * h2 + 60 * m2 + s2

    start_h, start_m, start_s = get_angles(h1, m1, s1)
    if start_h == start_s or start_m == start_s:
        count += 1

    for time in range(start_time + 1, end_time + 1):
        prev_hms = to_hms(time - 1)
        prev_angles = get_angles(*prev_hms)

        cur_hms = to_hms(time)
        cur_angles = get_angles(*cur_hms)

        if h_crossed(prev_angles, cur_angles):
            count += 1
        if m_crossed(prev_angles, cur_angles):
            count += 1

        if cur_angles[0] == cur_angles[1]:
            count -= 1

    return count


def to_hms(time):
    h, m, s = time // 3600, (time % 3600) // 60, (time % 60)
    return (h, m, s)


def get_angles(h, m, s):
    # h_angle : 360°/12h = 30°/h, 1/2°/m, 1/120°/s
    h_angle = 30 * (h % 12) + (1/2) * m + (1/120) * s
    # m : 360°/60m = 6°/m, 1/10°/s
    m_angle = 6 * m + (1/10) * s
    # s : 360°/60s = 6°/s
    s_angle = 6 * s

    return (h_angle, m_angle, s_angle)


def h_crossed(prev, cur):
    prev_h, prev_m, prev_s = prev
    cur_h, cur_m, cur_s = cur

    if prev_h > prev_s and cur_h <= cur_s:
        return True

    # s_angle : 354° -> 0°
    if prev_s == 354 and prev_h > 354:
        return True

    return False


def m_crossed(prev, cur):
    prev_h, prev_m, prev_s = prev
    cur_h, cur_m, cur_s = cur

    if prev_m > prev_s and cur_m <= cur_s:
        return True

    # s_angle : 354° -> 0°
    if prev_s == 354 and prev_m > 354:
        return True

    return False
