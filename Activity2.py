# input

unit_consumed = int(input("Enter The Amount Of Unit Consumed: "))

if unit_consumed <= 50:
    result = (unit_consumed * 2.60) + 25
    print (f"Your Bill Is {result} BDT")

elif unit_consumed > 50 and unit_consumed < 100:
    result = (unit_consumed * 3.25) + 35
    print (f"Your Bill Is {result} BDT")

elif unit_consumed > 100 and unit_consumed < 200:
    result = (unit_consumed * 5.26) + 45
    print (f"Your Bill Is {result} BDT")

elif unit_consumed > 200:
    result = (unit_consumed * 8.45) + 75
    print (f"Your Bill Is {result} BDT")

else:
    print ("ERROR")