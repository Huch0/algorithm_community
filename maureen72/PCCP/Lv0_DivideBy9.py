def solution(number):

    sum = 0
    for digit in number:
        value = int(digit)
        sum += value
        
    anw = sum % 9
    
    return anw
