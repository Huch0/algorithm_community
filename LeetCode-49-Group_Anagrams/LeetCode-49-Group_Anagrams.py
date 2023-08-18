class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = {}
        
        for string in strs:
            key = ''.join(sorted(string))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(string)
        
        result = []

        for list in anagrams.values():
            result.append(list)

        print(result)