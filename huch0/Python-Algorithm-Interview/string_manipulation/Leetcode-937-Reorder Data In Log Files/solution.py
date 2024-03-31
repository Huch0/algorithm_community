class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []

        # iterate logs and classify each logs.
        for log in logs:
            if(log.split(' ')[1][0].isalpha()):
                letter_logs.append(log)
            else:
                digit_logs.append(log)

        # Sort letter-logs lexicographically by content and identifier
        letter_logs.sort(key=lambda log: (log.split(' ')[1:], log.split(' ')[0]))

        # Join two lists
        return letter_logs + digit_logs