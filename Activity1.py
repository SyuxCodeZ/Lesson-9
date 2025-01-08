# the inputs

medcause = input("Do You Have A Medical Cause (Y for yes and N for no): ")

att = int(input("Enter Your Attendance: "))

# conditional statements

if medcause == "Y":
    print ("Allowed")
else:
        if att >= 75:
            print ("Allowed")

        else:
            print("Not Allowed")

