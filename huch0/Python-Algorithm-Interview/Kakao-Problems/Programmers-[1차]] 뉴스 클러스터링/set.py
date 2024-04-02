import collections


def solution(str1, str2):
    return J(to_mset(str1), to_mset(str2))


def to_mset(s):
    mset = []
    for i in range(len(s) - 1):
        elem = s[i:i + 2]
        if elem.isalpha():
            mset.append(elem.lower())
    return mset


def J(A, B) -> int:
    if len(A) == 0 and len(B) == 0:
        return 65536

    set_A = set(A)
    set_B = set(B)

    cnt_A = collections.Counter(A)
    cnt_B = collections.Counter(B)

    union_set = set_A.union(set_B)
    inter_set = set_A.intersection(set_B)

    union_ms_len = 0
    inter_ms_len = 0

    for u in union_set:
        union_ms_len += max(cnt_A[u], cnt_B[u])
        if u in inter_set:
            inter_ms_len += min(cnt_A[u], cnt_B[u])

    return int(inter_ms_len / union_ms_len * 65536)
