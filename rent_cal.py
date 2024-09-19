rent = int(input("Enter your room/flat rent ="))
food = int(input("Enter the amount of food ordered ="))
electricity_spend = int(input("Enter the total of electricity spend in units= "))

charge_per_unit = int(input("Enter the charge per unit ="))

person = int(input("enter the number of persons living in the room/flat ="))

total_bill = electricity_spend * charge_per_unit
output = (food + rent + total_bill) // person

print("Each person will pay = ", output)