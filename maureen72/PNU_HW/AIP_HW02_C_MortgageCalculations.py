def main():
    ## Analyze monthly payment of mortgage. 
    annualRateOfInterest, monthlyPayment, begBalance = inputData()
    (intForMonth, redOfPrincipal, endBalance)= calculateValues(annualRateOfInterest, monthlyPayment, begBalance)
    displayOutput(intForMonth, redOfPrincipal, endBalance)

def inputData() :  # 입력받기
    annualRateOfInterest = int(input("annual rate of interest: ")) # 연 이자율
    monthlyPayment = int(input("Enter monthly payment: ")) # 월 상환액
    begBalance = int(input("Enter beg. of month balance: ")) # 월 초 대출 잔액
    return annualRateOfInterest, monthlyPayment, begBalance

def calculateValues(annualRateOfInterest, monthlyPayment, begBalance) : 
    intForMonth = begBalance * (annualRateOfInterest / 100) / 12 # 월 이자 계산, 100을 나누는 이자율을 백분율로 표현한걸 소수로 바꿔서 계산해야하기 떄문
    redOfPrincipal = monthlyPayment - intForMonth # 월 상환 계산
    endBalance = begBalance - redOfPrincipal # 남은 돈 계산
    return intForMonth, redOfPrincipal, endBalance

def displayOutput(intForMonth, redOfPrincipal, endBalance) : # 출력하기
    print("Interest paid for the month: ${:,.2f}".format(intForMonth)) 
    print("Reduction of principal: ${:,.2f}".format(redOfPrincipal))
    print("End of month balance: ${:,.2f}".format(endBalance))

main()