def saparate_identifier_in_log(log : str) -> str:
    str_list = log.split()
    identifier = str_list[0]
    result = " ".join(str_list[1:])
    return [identifier, result]

class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        number_logs = []

        logs_copy = logs[:]  # 원래 리스트를 복사하여 사용
        #pop number_log
        for log in logs_copy:
            if '0' <= log.split()[1][0] <= '9':
                number_logs.append(log)
                logs.remove(log)
        
        for i in range(len(logs)):
            for j in range(i+1, len(logs)): 
                iden_i = saparate_identifier_in_log(logs[i])[0]
                iden_j = saparate_identifier_in_log(logs[j])[0]
                str_i = saparate_identifier_in_log(logs[i])[1]
                str_j = saparate_identifier_in_log(logs[j])[1]

                if (str_i > str_j):
                    logs[i], logs[j] = logs[j], logs[i]

                elif (str_i == str_j):
                    if (iden_i > iden_j):
                        logs[i], logs[j] = logs[j], logs[i]
                    else:
                        pass
                
                else:
                    pass

        logs += number_logs

        return logs