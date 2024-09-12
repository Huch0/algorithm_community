# input purchase price
purchasePrice = float(input("Enter purchase price: "))

# input selling price
sellingPrice = float(input("Enter selling price: "))

# set Markup
markup = sellingPrice - purchasePrice
print("Markup: ${}".format(markup))

# set percentage markup
percentageMarkup = markup / purchasePrice * 100
print("Percentage markup: {}%".format(percentageMarkup))

profit = markup / sellingPrice * 100
print("Profit margin: {:.2f}%".format(profit))