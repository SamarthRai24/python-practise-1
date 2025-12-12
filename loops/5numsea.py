tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
print (tup)
x = int(input("Enter the element, you want to check in this tuple : "))

i = 0
while i <= 9 :
    if x == tup[i]:
        print("Element found")
        break
    i += 1

else :
    print("No element found")

   