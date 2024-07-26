# 2
# 6
# 12

N = int(input())
query = []
for i in range(N):
    query.append(int(input()))

m_q = max(query)
D = [1 for _ in range(m_q + 1)]

if m_q >= 4:
    D[4] = 2
if m_q >= 5:
    D[5] = 2

if m_q >= 6:
    for i in range(6, m_q+1):
        D[i] = D[i-1] + D[i-5]

for q in query:
    print(D[q])