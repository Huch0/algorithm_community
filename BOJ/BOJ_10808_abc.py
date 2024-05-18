alphabet_count = [0 for _ in range(26)]
word = input()

for i in range(len(word)):
    alphabet_count[ord(word[i])-97] += 1

print(" ".join(map(str,alphabet_count)))