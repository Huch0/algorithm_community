class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answers = [0] * len(temperatures)
        for i in range(len(temperatures)):
            daysToGo = 0
            today = temperatures[i]
            for j in range(i, len(temperatures)):
                futureDate = temperatures[j]
                higher = futureDate - today
                if (higher > 0):
                    daysToGo = j - i
                    answers[i] = daysToGo
                    break  
        return(answers)