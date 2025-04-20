rollno =int(input("Enter the Roll Number: "))
name =input("Enter Name: ")
gender =input("Enter Gender: ")
standard =input("Enter Class: ")
english =int(input("Enter the English Number: "))
math =int(input("Enter the Math Number: "))
physics =int(input("Enter the Physics Number: "))
chemistry =int(input("Enter the Chemistry Number: "))
urdu =int(input("Enter the Urdu Number: "))
obtained_marks = english + math + physics + chemistry + urdu 
percentage = obtained_marks / 500 * 100


print("--------------STUDENT'S MARKSHEET-------------") 
print("your Roll Number is : " +str( rollno))
print("Your Name is : " + name)
print("Your Gender is :  " + gender)
print("Your Class is : " +  str(standard))
print("Total Marks are : 500 ")
print("Obtained Marks are : "+str(obtained_marks))
print("Your Percentage is : " + str(percentage))

if percentage >= 80:
    print("Grade: A+1")
    print("Remarks : Marvellous") 
elif percentage >= 70:
    print("Grade:A")    
    print("Remars : Excellent")
elif percentage >= 60:
    print("Grade : B")
    print("Remarks : Good")
elif percentage >= 50:
    print("Grade : C")
    print("Remarks : Fair")
elif percentage >= 40:
    print("Grade : D")
    print ("Remarks :Need Improvement ")
    
else:
    print("Grade : F (Fail)")          
    print ("Remarks : Failure")
        

i = 0
subjects_name = ""  

if english < 33: 
    i  = i + 1
    subjects_name += "English"

if math < 33:
    i = i + 1
    subjects_name +="Math"

if physics < 33:
    i = i + 1
    subjects_name += "Physics"

if chemistry < 33:
    i = i + 1
    subjects_name += "Chemistry"
if urdu < 33:
    i = i + 1
    subjects_name += "Urdu"

print("Failed Subjects Count: " + str(i))
print("Failed subjects Name: " + subjects_name)