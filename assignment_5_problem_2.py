
partno = int(input("Enter the part number"))
qty = input("Enter quantity to purchase")

if partno == 10 or partno == 55:
    unitprice = 1.00
elif partno == 90:
    unitprice = 2.00
elif partno == 70 or partno ==80:
    unitprice = 3.00
else:
    unitprice = 5.0

total = float(qty) * unitprice

print("Part number:     ",partno)
print("Unitprice:     ", unitprice)
print("total:     ",total)