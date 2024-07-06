# 11
# 1 4
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 8 12
# 2 13
# 12 14

# N = int(input())

# meetings = []

# for _ in range(N):
#     s, e = map(int, input().split())

#     meetings.append((s, e))

# def crush(meet):
#     i = 0
#     for index in range(len(meetings)):
#         if meetings[index] == meet:
#             i = index
#             break

#     if meet[0] == meet[1]:
#         return meetings.count(meet)
    
#     meetings_cutted = meetings[:i] + meetings[i+1:]
#     meetings_crushed = []

#     for m in meetings_cutted:
#         if m[0] <= meet[0] < m[1]  or m[0] < meet[1] <= m[1]:
#             meetings_crushed.append(m)

#     return meetings_crushed

# meetings.sort(key=lambda x : (len(crush(x)), -x[1] + x[0]))

# count = 0
# while meetings:
#     crushed = crush(meetings[-1])
#     for c in crushed:
#         meetings.remove(c)

#     meetings.pop()
#     meetings.sort(key=lambda x : (len(crush(x)), -x[1] + x[0]))

#     count += 1

# print(count)


N = int(input())

meetings = []

for _ in range(N):
    s, e = map(int, input().split())

    meetings.append((s, e))

meetings.sort(key=lambda x : (x[1], x[0]))

count = 0
i = 0

#print(meetings)
while i < len(meetings):
    #print(meetings[i])
    lower_bound = meetings[i][1]
    i += 1
    count += 1
    while i < len(meetings) and (meetings[i][0] < lower_bound):
        i += 1
    
print(count)