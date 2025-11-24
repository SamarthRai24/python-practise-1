x = int(input("Coordinate 1 : "))
y = int(input("Coordinate 2 : "))

if (x > 0 and y > 0):
    print ("Quadrant 1")
elif (x < 0 and y > 0):
    print ("Quadrant 2")
elif (x < 0 and y < 0):
    print ("Quadrant 3")
elif (x > 0 and y < 0):
    print ("Quadrant 4")
elif (x != 0 and y == 0):
    print ("On X Axis")
elif (x == 0 and y != 0):
    print ("On Y Axis")
else :
    print ("Origin")