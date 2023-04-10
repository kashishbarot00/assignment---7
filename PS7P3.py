#start
loop = input("Do you want to start the program? (Yes/No): ")

counter = 0

while loop.lower() == "yes":
  
    lname = input("Enter student last name: ")
    score1 = float(input("Enter exam 1 score: "))
    score2 = float(input("Enter exam 2 score: "))

    avg = (score1+ score2) / 2

   
    print("Student:" , lname)
    print("Average Exam Score: " , avg)

    counter = counter + 1

    loop = input("Do you want to enter data for another student? (Yes/No): ")

print("Number of Students: " , counter)
