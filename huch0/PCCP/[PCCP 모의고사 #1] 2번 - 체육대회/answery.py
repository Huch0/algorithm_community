def solution(ability):
    def dfs(num_selected, selected, ability_sum):

        if num_selected == len(ability[0]):
            ability_sums.append(ability_sum)
            return

        for i in range(len(ability)):
            if i not in selected and ability[i][num_selected] > 0:
                selected.append(i)
                dfs(num_selected + 1, selected,
                    ability_sum + ability[i][num_selected])
                selected.pop()

    ability_sums = []  # 최대 능력치 합을 저장할 변수

    num_students = len(ability)
    num_sports = len(ability[0])

#     for j in range(num_sports):
#         sorted_ability = sorted(ability, key=lambda x: x[j], reverse=True)

#         for i in range(num_sports, num_students):
#             sorted_ability[i][j] = 0

#     ability = sorted_ability

    dfs(0, [], 0)

    return max(ability_sums)
