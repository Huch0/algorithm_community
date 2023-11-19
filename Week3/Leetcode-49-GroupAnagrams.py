class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str_list = []
        word_list = []
        for word in strs:
            sorted_word_and_word = []
            sorted_word = ''.join(sorted(word))
            sorted_word_and_word.append(sorted_word)
            sorted_word_and_word.append(word)
            word_list.append(sorted_word_and_word)
        
 
            if sorted_word in sorted_str_list :
                pass
            else : sorted_str_list.append(sorted_word)
        

        dic = {string : [] for string in sorted_str_list}
        print(dic)
        print(word_list)

        for word in word_list :
            for sorted_word in dic.keys():
                if word[0] == sorted_word :
                    dic[sorted_word].append(word[1])
        
        result = []

        for i in dic.keys() :
            result.append(dic[i])
        
        return result
   