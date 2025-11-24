password = input("Password : ")

if (8 > len(password)):
    print ("Very Weak")
elif (11 > len(password) >= 8):
    print ("Weak")
elif (14 > len(password) >= 11):
    print ("Moderate")
else :
    print ("Strong")