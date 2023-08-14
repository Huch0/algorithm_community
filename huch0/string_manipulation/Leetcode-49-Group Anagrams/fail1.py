class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            anagram_set = collections.Counter(word)
            char_list = []
            for key, value in anagram_set.items():
                char_count_str = key + str(value)
                char_list.append(char_count_str)
            
            anagram_key = str(set(char_list))

            anagram_map[anagram_key].append(word)
        
        output_list = []
        
        print(anagram_map)

        for key, value in anagram_map.items():
            output_list.append(value)
            print(value)

        return output_list

