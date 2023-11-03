class Solution(object):
    def reorderLogFiles(self, logs):
        word, num= [], []
        for log in logs:
            if log.split()[1].isalpha():
                word.append(log)
            else:
                num.append(log)

        word.sort(key=lambda x: (x.split()[1:], x.split()[0]))
         
        return word + num        