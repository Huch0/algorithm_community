class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        str_list = []
        digit_list = []
        
        for i in logs :
            if i.split()[1].isdigit() : digit_list.append(i)
            else : str_list.append(' '.join(i.split()[1:]) + ' / ' + i.split()[0])
                
        str_list.sort()

        for index,i in enumerate(str_list):
            str_list[index] = i.split()[-1] + ' ' + ' '.join(i.split()[:-2])

        result = []
        
        for i in str_list:
            result.append(i)
        for i in digit_list:
            result.append(i)
        
        return result