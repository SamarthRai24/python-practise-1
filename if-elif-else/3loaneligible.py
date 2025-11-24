credit = int(input("Credit Score : "))
income = int(input("Annual Income : $"))
loan = int(input("Exisiting Loans : "))

if (750 < credit and 50000 < income):
    print ("Eligible")
elif (650 > credit and 2 < loan):
    print ("Not Eligible")
elif (750 > credit > 650 and 50000 > income > 30000):
    print ("Review Required")
else :
    print ("Not Eligible")