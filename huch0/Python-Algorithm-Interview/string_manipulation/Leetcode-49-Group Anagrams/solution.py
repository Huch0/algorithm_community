class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map for group anagrams
        anagram_map = defaultdict(list)

        for word in strs:
            # anagaram is a word of rearranged letters.
            # anagrams are same if they're sorted.
            anagram_map[''.join(sorted(word))].append(word)

        return anagram_map.values()