# start 
loop = input("Do you want to start the program? (Yes/No): ")

total_discount = 0


while loop.response() == "yes":
    
    quantity = float(input("Enter quantity: "))
    price = float(input("Enter price: "))

    extprice = quantity * price

    if extprice > 10000.00:
        discpercent = 0.25
    else:
        discpercent = 0.10
    discamt = extprice * discpercent

    total = extprice - discamt

   
    total_discount += discamt

    print("Extended Price:" , extprice)
    print("Discount Amount:" , discamt)
    print("Total: " , total)

    loop = input("Do you want to enter data for another order? (Yes/No): ")

#Total discount
print("Total Discount: " , total_discount)
