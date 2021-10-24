Apple = float(input("Enter apple quantity: "))
Orange = float(input("Enter orange quantity: "))
AppleCost= 20.00* Apple
OrangeCost= 25.00* Orange
TotalAmount= AppleCost + OrangeCost

format_TotalAmount= "{: .2f}".format(TotalAmount)
float_TotalAmount = float(format_TotalAmount)
print("Total Amount is: ", format_TotalAmount)