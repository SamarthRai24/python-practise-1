a = input("Enter 1st element : ")
b = input("Enter 2nd element : ")
c = input("Enter 3rd element : ")
d = input("Enter 4th element : ")

list = [a, b, c, d]
list1 = list.copy()
list1.reverse()

if(list == list1):
    print("Yes, this is Palindrome")
else:
    print("No, this is not Palindrome")

print(list)
print(list1)