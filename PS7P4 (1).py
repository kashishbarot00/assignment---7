#Start
loop = input("Do you want to start the program? (Yes/No): ")


sumofgrosspay = 0
noofemployees = 0


while loop.lower() == "yes":
   
    lname = input("Enter employee last name: ")
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter pay rate: "))

    
    if hours > 40:
        grosspay = (40 * rate ) + (hours - 40 * 1.5)
      
    else:
        grosspay = hours * rate

    
    sumofgrosspay =  sumofgrosspay + grosspay
    noofemployees = noofemployees + 1

    print("Employee: " ,lname)
    print("Gross Pay: $" , grosspay)

    
    loop = input("Do you want to enter data for another employee? (Yes/No): ")


avggrosspay = sumofgrosspay / noofemployees
print("Total Gross Pay: " , sumofgrosspay)
print("Number of Employees: " , noofemployees)
print("Average Gross Pay: $ " , avggrosspay)
#End