class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        number_logs = []
        char_logs = []

        for log in logs:
            if log.split()[1].isdigit():
                number_logs.append(log)
            else:
                char_logs.append(log)

        char_logs.sort(key = lambda x : (x.split()[1:], x.split()[0]))
        
        return char_logs + number_logs
                
