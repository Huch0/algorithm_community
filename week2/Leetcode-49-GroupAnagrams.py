class Solution(object):
    def groupAnagrams(self, strs):
        anagram = {}
        
        for word in strs:
            sortedWord = ''.join(sorted(word))
            #print(sortedWord)

            if sortedWord in anagram:
                anagram[sortedWord].append(word)
            else:
                anagram[sortedWord] = [word]
            #print(anagram)
        result = list(anagram.values())

        return result  