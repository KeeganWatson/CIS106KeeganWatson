lastname = input("Enter Last Name")
grosspay = input("Enter Your Gross Pay")
nodep = input("enter dependents")

adjgross = float(grosspay) - 12000.00 * float(nodep)

if adjgross > 50000.00:
  tax = adjgross * 0.20
else:
  tax = adjgross * 0.10

if tax < 0:
  tax = 100.00

print (lastname)
print ("Gross Income:       $", grosspay)
print ("Number of Depeendents: ", nodep)
print ("Adjusted Gross:       $", adjgross)
print ("Income Tax:          $", tax)