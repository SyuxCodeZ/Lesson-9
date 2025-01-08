#the input

select = input("Enter Your Ride Selection (Bike Or Car): ")

if select == "bike":
    select2 = input("what type of bike? (motorbike or normal bike): ")
    print ("Your Ride Is On The Way!")

elif select == "car":
    select2 = input("what type of car? (SUV or a normal car): ")
    print ("Your Ride Is On The Way!")

else:
    print ("ERROR")