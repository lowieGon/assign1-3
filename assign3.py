Money = float(input("Enter available money: "))
Apple = float(input("Enter price of Apple: "))
AppleQty = Money / Apple
Change = Money % AppleQty
print(f"You can buy {AppleQty} and your change is {Change}")