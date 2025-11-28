c = int(input("Cart Total : ")) #c=Cart Total
l = input("Loyalty Status Gold/Silver/Bronze : ") #l=loyalty badge

if(c >= 5000):
    print ("Premium Order")
    if(l == "Gold" or "gold" or "GOLD"):
        print (c * 0.8)
        print ("Shipping Free")
    elif(l == "Silver" or "silver" or "SILVER"):
        if(c >= 10000):
            print (c * 0.85)
            print ("Shipping Free")
    else:
        print (c * 0.9)
        print ("Shipping Free")
else:
    print ("Standard Order")
    print ("Shipping Charges 200")