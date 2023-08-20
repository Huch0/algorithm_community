class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        words = []
        lowered = paragraph.lower()
        lowered += " "
        splitPointer = 0
        
        for i in range(len(lowered)-1):
            if lowered[i].isalpha() and not lowered[i+1].isalpha():
                words.append(lowered[splitPointer:i+1])
            elif not lowered[i].isalpha() and lowered[i+1].isalpha():
                splitPointer = i+1

        words = [word for word in words if word not in banned]
        words.sort()
        splitPointer = 0
        changing = 0
        mostCommonIndex = 0
        mostCommon = 0
        for i in range(len(words)-1):
            if words[i] != words[i+1]:
                changing = i - splitPointer
                splitPointer = i+1
                if changing > mostCommon:
                    mostCommon = changing
                    mostCommonIndex = i
            
        return words[mostCommonIndex]

# class Solution(object):
#     def mostCommonWord(self, paragraph, banned):
#         words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
#         .lower().split()
#             if word not in banned]

#         counts = collections.Counter(words)

#         return counts.most_common(1)[0][0]