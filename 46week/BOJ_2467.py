# 5
# -99 -2 -1 4 98

# -> -99 98

# N = int(input())
# solutions = list(map(int, input().split()))

# def find_closest_target(i, target):
#     # solutions_removed = solutions[:i] + solutions[i+1:]
#     st = 0
#     en = N
    
#     while st < en:
#         mid = (st + en) // 2
#         if solutions[mid] < target:
#             st = mid + 1
#         # elif solutions[mid] == target:

#         #     return target
#         elif solutions[mid] >= target:
#             en = mid
            
    

#     if st == i:
#         if st == len(solutions):
#             return solutions[-2]
#         elif st == 0:
#             return solutions[1]
        
#         if abs(target - solutions[st+1]) < abs(target - solutions[st-1]):
#             return solutions[st+1]
#         else:
#             return solutions[st-1]
#     else:
#         if st == len(solutions):
#             return solutions[-1]
#         elif st == 0:
#             return solutions[st]
        
#         if solutions[st] == target:
#             return solutions[st]
#         else:
#             if abs(target - solutions[st]) < abs(target - solutions[st-1]):
#                 return solutions[st]
#             else:
#                 return solutions[st-1]
        
# min_comb = None
# for i in range(N):
#     target = -1 * solutions[i]
#     best_right = find_closest_target(i, target)
#     print(f"left : {-1 * target}, right: {best_right}")
#     if not min_comb:
#         min_comb = (solutions[i], best_right)
#     else:
#         cur_best = abs(min_comb[0] + min_comb[1])
#         if cur_best == 0:
#             break
#         if abs(solutions[i] + best_right) < cur_best:
#             min_comb = (solutions[i], best_right)


# print(min_comb[0], min_comb[1])

import bisect

N = int(input())
solutions = list(map(int, input().split()))

ans1 = int(1e9) + 1
ans2 = int(1e9) + 1

for i in range(N):
    target = -solutions[i]
    idx = bisect.bisect_left(solutions, target)
    
    # a[idx+1] 또는 a[idx] 또는 a[idx-1]에서 가장 가까운 값을 찾는다.
    if idx + 1 < N and i != idx + 1 and abs(solutions[i] + solutions[idx + 1]) < abs(ans1 + ans2):
        ans1 = solutions[i]
        ans2 = solutions[idx + 1]
    
    if idx < N and i != idx and abs(solutions[i] + solutions[idx]) < abs(ans1 + ans2):
        ans1 = solutions[i]
        ans2 = solutions[idx]
    
    if idx > 0 and i != idx - 1 and abs(solutions[i] + solutions[idx - 1]) < abs(ans1 + ans2):
        ans1 = solutions[i]
        ans2 = solutions[idx - 1]

if ans1 > ans2:
    ans1, ans2 = ans2, ans1

print(ans1, ans2)
