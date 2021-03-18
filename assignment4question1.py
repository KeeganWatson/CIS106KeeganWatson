quantity = float(input("Enter Quantity"))
tax = .07
unitprice = 5
adjgross = float(quantity) * float(unitprice) + float(tax) * (float(quantity) * float(unitprice))

if quantity > 1000.00:
 float(unitprice = 3.00)
else:
 unitprice = 5.00

print ("total:   $",adjgross)
print ("Unit price:    $",unitprice)
print ("Tax:    7%")
print ("Quantity:    ",quantity)