n = int(input())

perms = []


def perm(seq):
    if len(seq) == n:
        perms.append(seq)
        return

    for i in range(1, n + 1):
        if i not in seq:
            perm(seq + [i])


perm([])

for perm in perms:
    print(' '.join(map(str, perm)))
