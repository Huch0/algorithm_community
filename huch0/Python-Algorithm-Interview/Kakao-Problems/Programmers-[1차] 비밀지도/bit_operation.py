def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        answer_i = ""
        j = 0
        while j < n:
            if (arr1[i] & 1) or (arr2[i] & 1):
                answer_i = '#' + answer_i
            else:
                answer_i = ' ' + answer_i

            arr1[i] >>= 1
            arr2[i] >>= 1
            j += 1

        answer.append(answer_i)

    return answer
