# input initial salary
beginningSalary = float(input("Enter beginning salary: "))

# change rate -> 5% raise 하면 1.05를 곱해야하는데 four successive라 했기때문에 이것까지 반영
changeRate = (1.05)**4

#new salary
newSalary = beginningSalary * changeRate

# output
print("New salary: ${:,.2f}".format(newSalary))
print("Change: {:.2f}%".format(changeRate*100 - 100))