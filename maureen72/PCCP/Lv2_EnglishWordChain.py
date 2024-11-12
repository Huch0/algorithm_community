def solution(n, words):
    used_words = set()
    
    for i in range(len(words)):
        current_word = words[i]
        if (current_word in used_words) or (i > 0 and words[i-1][-1] != current_word[0]):
            # 사람의 번호와 차례 계산
            person = (i % n) + 1
            turn = (i // n) + 1
            return [person, turn]

        used_words.add(current_word)
    return [0, 0]
