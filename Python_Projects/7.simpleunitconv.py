
# Welcome Page
print("Welcome to the Simple Unit Converter!")

print("We can help you convert your units.")

# functions for weight converter
def convert_weight(value, unit):
    if unit.lower() == "lb":
        return round(value * 0.453592, 2), "kg"
    elif unit.lower() == "kg":
        return round(value / 0.453592, 2), "lb"

def convert_temp(value, unit):
    if unit.lower() == "c":
        return round((value * 9/5) + 32, 2), "F"
    elif unit.lower() == "f":
        return round((value - 32) * 5/9, 2), "C"

def convert_length(value, unit):
    if unit.lower() == "miles":
        return round(value * 0.621371, 2), "KM"
    elif unit.lower() == "km":
        return round( value * 1.60934, 2), "MILES"

while True:
    unit = input("Enter your unit you wish to be converted (lb/kg) or (C/F) or (miles/km) or (q) to exit: ").upper()


    if unit.lower() == "q":
        print("You have ended the app! Goodbye")
        break
        # stops the loop

    value = float(input("Enter the value you wish to convert: "))

    if unit.lower() in ["lb", "kg"]:
        print("You have selected Weight.")
        result_weight, target_unit = convert_weight(value,unit)
        print(f"{value} {unit} in {target_unit.upper()} is {result_weight}")

    elif unit.lower() in ["c", "f"]:
        print("You have selected Temperature.")
        result_temp, target_unit = convert_temp(value,unit)
        print(f"{value} {unit} in {target_unit.upper()} is {result_temp}")

    elif unit.lower() in ["miles", "km"]:
        print("You have selected Lenght.")
        result_length, target_unit = convert_length(value, unit)
        print(f"{value} {unit} in {target_unit.upper()} is {result_length}")

    else:
        print("Invalid option, please try again!")


            






