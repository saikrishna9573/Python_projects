weight = int(input("Enter your weight "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    final = float(weight * 2.2046226218)
    print("Weight in lbs is " + str(final) + "lbs")
elif unit.upper() == "L":
    final1 = float(weight / 2.2046226218)
    print("Weight in lbs is " + str(final1) + "kgs")