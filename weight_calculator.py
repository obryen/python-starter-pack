weight = input("please enter your weight: ")
unit_of_measure = input("Select unit of measure (K) for kg or (G) for grams: ")

standardized_measure = unit_of_measure.lower()
if standardized_measure == "k":
    print("weight in kg:",float(weight))
elif standardized_measure == "g":
    print("wight in grams:", float(weight)* 1000)
else:
    print("invalid input bro")