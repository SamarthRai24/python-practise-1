p = int(input("High School Percentage : ")) #p=percentage
a = int(input("Overall Attendance : ")) #a=attendance
c = float(input("Last CGPA : ")) #c=cgpa

if(p >= 85):
    if(a >= 90):
        if(c >= 8.5):
            print ("Congratulations! Eligible for Super-Star Scholarship")
        elif(8.5 > c >= 7):
            print ("Eligible for Enhanced Scholarship")
        else:
            print ("Eligible for Basic Scholarship Only")
    elif(90 > a > 80):
        print ("Eligible for Basic Scholarship Only")
    else:
        print ("Not Eligible: Poor Attendance")
else:
    print ("Not Eligible: Low Percentage")