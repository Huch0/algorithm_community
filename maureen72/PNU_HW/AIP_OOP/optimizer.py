from setup import Setup

class HillClimbing(Setup):
    def __init__(self):
        # 1. Setup에 정의된 delta, alpha, dx에 접근하기 위해 Setup 초기화
        # 2. self._pType 정의하기 (Tsp인지, Numeric인지 구분하기 위한 Integer 변수 선언)
        # 3. self._limitStuck 정의하기 (지금은 First-choice에서만 사용하지만, 앞으로 추가될
        # 다른 hillclimbing 알고리즘에서 사용함)
        Setup.__init__(self)
        self._pType = 0
        self._limitStuck = 100

    def setVariables(self, pType):
        # 1. pType을 인자로 받아서 self._pType에 assign
        self._pType = pType

    def displaySetting(self):
        # 1. pType==1 (Numeric) 일 때만, Mutation step size를 출력하는 함수
        # first-choice.py 코드의 ‘print(＂Mutation step size:＂, p.getDelta())’ 부분 활용
        if self._pType == 1:
            print("Mutation step size:", self._delta)

    def run(self):
        pass


class FirstChoice(HillClimbing):
    def displaySetting(self):
        # first-choice.py 코드의 displaySetting 부분 활용
        # HillClimb에 정의했던 displaySetting을 Super를 통해 호출해서 구현하기
        print()
        print("Search algorithm: First-Choice Hill Climbing")
        super().displaySetting()
        print("Max evaluations with no improvement: {0:,} iterations".format(self._limitStuck))

        
    def run(self, p):
        # first-choice.py에 정의했던 firstchoice 함수를 활용해서 구현
        current = p.randomInit()
        valueC = p.evaluate(current)
        i = 0
        while i < self._limitStuck:
            successor = p.randomMutant(current)
            valueS = p.evaluate(successor)
            if valueS < valueC:
                current = successor
                valueC = valueS
                i = 0
            else:
                i += 1
        p.storeResult(current, valueC)

class SteepestAscent(HillClimbing):
    def displaySetting(self):
        print()
        print("Search algorithm: Steepest-Ascent Hill Climbing")
        return super().displaySetting()
    
    def run(self, p):
        current = p.randomInit() # 'current' is a list of values
        valueC = p.evaluate(current)
        while True:
            neighbors = p.mutants(current)
            successor, valueS = self.bestOf(neighbors, p)
            if valueS >= valueC:
                break
            else:
                current = successor
                valueC = valueS
        p.storeResult(current, valueC)

    def bestOf(self, neighbors, p):
            best = neighbors[0]
            bestValue = p.evaluate(best)
            for i in range(1, len(neighbors)):
                newValue = p.evaluate(neighbors[i])
                if newValue < bestValue:
                    best = neighbors[i]
                    bestValue = newValue # 새로운 값이 더 작으면(더 좋은 것이기때문에) 바꿔주기

            return best, bestValue
    

class GradientDescent(HillClimbing):

    def displaySetting(self):
        print()
        print("Search algorithm: Gradient Descent")
        print()
        print("Udate rate:", self._alpha)
        print("Increment for calculating derivative:", self._dx)

    def run(self,p):
        currentP = p.randomInit()  # Current point
        valueC = p.evaluate(currentP)
        while True:
            nextP = p.takeStep(currentP, valueC)
            valueN = p.evaluate(nextP)
            if valueN >= valueC:
                break
            else:
                currentP = nextP
                valueC = valueN
        p.storeResult(currentP, valueC)