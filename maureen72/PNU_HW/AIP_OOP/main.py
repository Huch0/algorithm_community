from problem import *
from optimizer import *

def main():
    p, pType = selectProblem()
    alg = selectAlgorithm(pType)
    # Call the search algorithm
    alg.run(p)
    # Show the problem solved
    p.describe()
    # Show the algorithm settings
    alg.displaySetting()
    # Report results
    p.report()


def selectProblem():
    print("Select the problem type:")
    print(" 1. Numerical Optimization")
    print(" 2. TSP")
    # 1 (Numeric) 또는 2 (TSP)를 입력 받아서 대응되는 Problem Class를 초기화해서 반환하기
    pType = int(input("Enter the number: "))
    if pType == 1:
        p = Numeric()
    elif pType == 2:
        p = Tsp()
    p.setVariables()
    return p, pType

def selectAlgorithm(pType):
    print()
    print("Select the search algorithm:")
    print(" 1. Steepest-Ascent")
    print(" 2. First-Choice")
    print(" 3. Gradient Descent")
    # pType == 2 (TSP)일 경우, Gradient Descent를 입력 받으면 사용자로부터 재입력 받도록 구현
    # pType과 aType이 올바르게 설정 됐는지 확인하기 위한 invalid(pType, aType) 함수 추가 구현
    while True:
        aType = int(input("Enter the number: "))
        if not invalid(pType, aType):
            break
    optimizers = { 1: 'SteepestAscent()', 2: 'FirstChoice()', 3: 'GradientDescent()' }
    alg = eval(optimizers[aType])
    alg.setVariables(pType)
    return alg

def invalid(pType, aType):
    if pType == 2 and aType == 3:
        print("You cannot choose Gradient Descent")
        print("   unless your want a function optimization")
        return True
    else:
        return False

main()