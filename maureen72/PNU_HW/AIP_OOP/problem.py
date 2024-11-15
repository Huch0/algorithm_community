import random
import math
from setup import Setup

# HW06에서 구현했던 problem.py코드에서 access method는 다 제거함
# 왜냐하면 Setup class에서 이를 구현했고, 이를 상속받아 사용하기 때문에
class Problem(Setup):
    def __init__(self):
        Setup.__init__(self)
        self._solution = []
        self._value = 0
        self._numEval = 0

    def setVariables(self):
        pass
    
    def randomInit(self):
        pass

    def evaluate(self):
        pass

    def mutants(self):
        pass

    def randomMutant(self, current):
        pass

    def describe(self):
        pass

    def storeResult(self, solution, value):
        self._solution = solution
        self._value = value

    def report(self):
        print()
        print("Total number of evaluations: {0:,}".format(self._numEval))


class Numeric(Problem):
    def __init__(self):
        Problem.__init__(self)
        self._expression = ''
        self._domain = []     # domain as a list
        self._delta = 0.01    # Step size for axis-parallel mutation

        #self._alpha = 0.01    # Update rate for gradient descent
        #self._dx = 10 ** (-4) # Increment for calculating derivative
    
    def setVariables(self):
        filename = input("Enter the file name of a function: ")
        infile = open(filename, "r")
        self._expression = infile.readline()
        varNames, low, up = [], [], [] # 각각 변수 이름, 최소값, 최대값을 저장할 리스트
        line = infile.readline()

        while line != "":
            data = line.split(",")
            varNames.append(data[0])
            low.append(eval(data[1]))
            up.append(eval(data[2]))
            line = infile.readline()
        infile.close()
        self._domain = [varNames, low, up] 
    
    #def getDelta(self): # new method 
        #return self._delta

    def describe(self): # describeProblem
        print()
        print("Objective function:")
        print(self._expression)
        print("Search space:")
        varNames = self._domain[0]
        low = self._domain[1]
        up = self._domain[2]
        for i in range(len(low)):
            print(" " + varNames[i] + ":", (low[i], up[i]))

    def report(self):
        print()
        print("Solution found: ")
        print(self.coordinate())
        print("Minimum value: {0:,.3f}".format(self._value))
        Problem.report(self)

    def coordinate(self):
        c = [round(value,3) for value in self._solution]
        return tuple(c)
    
    def randomInit(self):
        domain = self._domain
        low, up = domain[1], domain[2]
        init = []

        for i in range(len(low)):
            r = random.uniform(low[i], up[i])
            init.append(r)
        return init
    
    def evaluate(self, current):
        self._numEval += 1 # 총 eval 횟수 하나식 증가
        expr = self._expression 
        varNames = self._domain[0]
        for i in range(len(varNames)):
            assignment = varNames[i] + '=' + str(current[i]) # 변수명 = '값' 형태로 출력되게 설정
            exec(assignment) # 설정된 값을 실행
        return eval(expr) 
    
    def mutate(self, current, i, d):
        mutant = current[:]
        domain = self._domain
        l= domain[1][i]
        u = domain[2][i]
        if l <= (mutant[i] + d) <= u:
            mutant[i] += d
        return mutant
    
    # steepest-ascent
    def mutants(self, current): # steepest ascent (n)에서 Numeric problem 관련 함수를 numeric class로 이동
        neighbors = []
        for i in range(len(current)): # For each variable
            mutant = self.mutate(current, i, self._delta)
            neighbors.append(mutant)
            mutant = self.mutate(current, i, -self._delta)
            neighbors.append(mutant)
        return neighbors
    
    # first-choice
    def randomMutant(self, current): ###
        i = random.randint(0, len(current) - 1)  # 몇 번째 var를 변경할 것인지를 랜덤하게 지정
        if random.uniform(0,1) < 0.5: # 이때 D는 0.5의 확률로 증가할지 감소할지 결정되어야함
            d = self._delta
        else:
            d = - self._delta
            
        return self.mutate(current, i, d) 
    
    # gradient descent
    #def getAlpha(self): # self._alpha Accessor
        #return self._alpha
    
    #def getDx(self): # self._dx Accessor
       # return self._dx
    
    # gradient를 통해 next step을 계산
    # next step이 domain 범위 이내 일 때만 next step을 반환
    def takeStep(self, currentP, valueC):
        next = currentP[:] # 리스트 복사
        gradient = self.gradient(currentP,valueC) # gradient 값 계산
        for i in range(len(next)): # 각각의 변수에 대해
            next[i] -= self._alpha * gradient[i] # gradient 값에 따라 다음 step을 계산 -> w' = w - alpha*f'(w)
        if self.isLegal(next): # 새로 만들어진 값이 범위 내에 있다면 
            return next # 새로운 값을 반환
        else:
            return currentP # 범위 밖이면 원래 값을 반환
    
    # 주어진 변수 값들(x)이 도메인 범위 이내인지 확인하고 T/F를 반환
    def isLegal(self, x):
        low = self._domain[1]
        up = self._domain[2]
        for i in range(len(x)): # 각 변수에 대해 실행
            if(low[i] > x[i] or up[i] < x[i]): # 범위 밖이면
                return False # False 반환
        return True # 범위 안이면 True 반환
    
    # '각 변수'의 gradient를 list형으로 반환 
    def gradient(self, x, v): # x는 현재 변수 값, v는 현재 값 list
        gradient = [] # gradient 값을 저장할 리스트
        for i in range(len(x)): # 각 변수에 대해
            changedX = x[:] # 리스트 복사
            changedX[i] += self._dx # i번째 변수에 f(x+dx) 해주기
            gradient.append((self.evaluate(changedX) - v) / self._dx) # f'(x) = (f(x+dx) - f(x)) / dx 계산
        return gradient # gradient 값 반환
    
class Tsp(Problem):
    def __init__(self):
        Problem.__init__(self)
        self._numCities = 0
        self._locations = []       # A list of tuples
        self._distanceTable = []

    def setVariables(self):
        ## Read in a TSP (# of cities, locatioins) from a file.
        ## Then, create a problem instance and return it.
        fileName = input("Enter the file name of a TSP: ")
        infile = open(fileName, 'r')
        # First line is number of cities
        self._numCities = int(infile.readline())
        locations = []
        line = infile.readline()  # The rest of the lines are locations
        while line != '':
            locations.append(eval(line)) # Make a tuple and append
            line = infile.readline()
        infile.close()
        self._locations = locations
        self._distanceTable = self.calcDistanceTable()

    def calcDistanceTable(self):
            n = self._numCities
            locations = self._locations
            table = [[0] * n for _ in range(n)] # 2차원 리스트 초기화
            
            for i in range(n):
                for j in range(n):
                    if i != j:  # 같은 도시 간 거리는 계산하지 않음
                        table[i][j] = math.sqrt((locations[j][0] - locations[i][0]) ** 2 + 
                                                (locations[j][1] - locations[i][1]) ** 2) # 두 점 사이의 거리를 구하는 공식 사용해서 table에 저장
            return table  # A symmetric matrix of pairwise distances

    def randomInit(self):   # Return a random initial tour
        n = self._numCities
        init = list(range(n))
        random.shuffle(init)
        return init

    def evaluate(self, current): ###
        ## Calculate the tour cost of 'current'
        ## 'p' is a Problem instance
        ## 'current' is a list of city ids
        self._numEval += 1 # 총 eval횟수 늘이기
        n = self._numCities
        table = self._distanceTable
        cost = 0 # 비용 초기화

        # 첫 도시부터 맨 마지막 도시까지 투어하면서 distance table을 참고하여 비용 계산
        for i in range(n-1):
            locFrom = current[i]
            locTo = current[i+1]
            cost += table[locFrom][locTo]
        # 맨 마지막 도시에서 처음 도시로 돌아오는 비용을 고려해서 cost에 더해줌
        cost += table[current[-1]][current[0]]
        
        return cost
    
    #steepest-ascent
    def mutants(self, current): # Apply inversion
        n = self._numCities
        neighbors = []
        count = 0
        triedPairs = []
        while count <= n:  # Pick two random loci for inversion
            i, j = sorted([random.randrange(n) for _ in range(2)])
            if i < j and [i, j] not in triedPairs:
                triedPairs.append([i, j])
                curCopy = self.inversion(current, i, j)
                count += 1
                neighbors.append(curCopy)
        return neighbors

    def inversion(self, current, i, j):  # Perform inversion
        curCopy = current[:] # 리스트 복사
        while i < j:
            curCopy[i], curCopy[j] = curCopy[j], curCopy[i]
            i += 1
            j -= 1
        return curCopy

    #first-choice
    def randomMutant(self, current): # Apply inversion 
        while True:
            i, j = sorted([random.randrange(self._numCities) 
                        for _ in range(2)])
            if i < j:
                curCopy = self.inversion(current, i, j)
                break
        return curCopy

    def describe(self):
        print()
        n = self._numCities
        print("Number of cities:", n)
        print("City locations:")
        locations = self._locations
        for i in range(n):
            print("{0:>12}".format(str(locations[i])), end = '')
            if i % 5 == 4:
                print()

    def report(self):
        print()
        print("Best order of visits:")
        self.tenPerRow()       # Print 10 cities per row
        print("Minimum tour cost: {0:,}".format(round(self._value)))
        Problem.report(self)

    def tenPerRow(self):
        solution = self._solution
        for i in range(len(solution)):
            print("{0:>5}".format(solution[i]), end='')
            if i % 10 == 9: # 10개씩 출력 -> 줄바꿈
                print()
