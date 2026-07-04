import math

# ==============================
# NOT SO SIMPLE CALCULATOR
# Phase 1 - Main Menu
# ==============================

while True:
    print("\n" + "=" * 40)
    print("        NOT SO SIMPLE CALCULATOR")
    print("=" * 40)

    print("1. Basic Arithmetics")
    print("2. Advanced Arithmetics")
    print("3. Basic Conversions")
    print("4. Advanced Conversions")
    print("5. Tables")
    print("6. Perimeter Calculations")
    print("7. Area Calculations")
    print("8. Volume Calculations")
    print("9. Angular Calculations")
    print("10. Marks Calculations")
    print("11. Economic Calculations")
    print("12. SIP Calculations")
    print("0. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        
        while True:
            print("\n" + "=" * 40)
            print("      BASIC ARITHMETICS")
            print("=" * 40)

            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Percentage")
            print("0. Back to Main Menu")

            basic_choice = input("\nEnter your choice: ")

            if basic_choice == "1":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result =", a + b)

            elif basic_choice == "2":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result =", a - b)

            elif basic_choice == "3":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result =", a * b)

            elif basic_choice == "4":
                a = float(input("Enter dividend: "))
                b = float(input("Enter divisor: "))

                if b == 0:
                    print("Error! Division by zero is not allowed.")
                else:
                    print("Result =", a / b)

            elif basic_choice == "5":
                value = float(input("Enter the value: "))
                total = float(input("Enter the total value: "))

                if total == 0:
                    print("Error! Total cannot be zero.")
                else:
                    percentage = (value / total) * 100
                    print("Percentage =", percentage, "%")

            elif basic_choice == "0":
                break

            else:
                print("Invalid choice! Please try again.")

    elif choice == "2":
        while True:
            print("\n" + "=" * 40)
            print("     ADVANCED ARITHMETICS")
            print("=" * 40)

            print("1. Floor Division")
            print("2. Modulo")
            print("3. Reciprocal")
            print("4. Factorial")
            print("5. Square Root")
            print("6. Cube Root")
            print("7. Exponent")
            print("8. Natural Log (ln)")
            print("9. Log Base 2")
            print("10. Log Base 10")
            print("0. Back to Main Menu")

            adv_choice = input("\nEnter your choice: ")

            if adv_choice == "1":
                a = float(input("Enter dividend: "))
                b = float(input("Enter divisor: "))

                if b == 0:
                    print("Error! Division by zero is not allowed.")
                else:
                    print("Result =", a // b)

            elif adv_choice == "2":
                a = float(input("Enter dividend: "))
                b = float(input("Enter divisor: "))

                if b == 0:
                    print("Error! Division by zero is not allowed.")
                else:
                    print("Result =", a % b)

            elif adv_choice == "3":
                n = float(input("Enter a number: "))

                if n == 0:
                    print("Reciprocal of zero is undefined.")
                else:
                    print("Result =", 1 / n)

            elif adv_choice == "4":
                n = int(input("Enter a non-negative integer: "))

                if n < 0:
                    print("Factorial is not defined for negative numbers.")
                else:
                    print("Result =", math.factorial(n))

            elif adv_choice == "5":
                n = float(input("Enter a number: "))

                if n < 0:
                    print("Square root of a negative number is not a real number.")
                else:
                    print("Result =", math.sqrt(n))

            elif adv_choice == "6":
                n = float(input("Enter a number: "))
                print("Result =", n ** (1/3))

            elif adv_choice == "7":
                base = float(input("Enter the base: "))
                power = float(input("Enter the exponent: "))
                print("Result =", base ** power)

            elif adv_choice == "8":
                n = float(input("Enter a positive number: "))

                if n <= 0:
                    print("Natural logarithm is defined only for positive numbers.")
                else:
                    print("Result =", math.log(n))

            elif adv_choice == "9":
                n = float(input("Enter a positive number: "))

                if n <= 0:
                    print("Log base 2 is defined only for positive numbers.")
                else:
                    print("Result =", math.log2(n))

            elif adv_choice == "10":
                n = float(input("Enter a positive number: "))

                if n <= 0:
                    print("Log base 10 is defined only for positive numbers.")
                else:
                    print("Result =", math.log10(n))

            elif adv_choice == "0":
                break

            else:
                print("Invalid choice! Please try again.")

    elif choice == "3":
        while True:
            print("\n" + "=" * 40)
            print("      INTER-CONVERSIONS")
            print("=" * 40)

            print("1. Length")
            print("2. Area")
            print("3. Volume")
            print("4. Mass")
            print("5. Speed")
            print("6. Time")
            print("7. Temperature")
            print("0. Back to Main Menu")

            conv_choice = input("\nEnter your choice: ")

            if conv_choice == "1":

                units = {
                    "1": ("Nanometer (nm)", 1e-9),
                    "2": ("Micrometer (µm)", 1e-6),
                    "3": ("Millimeter (mm)", 1e-3),
                    "4": ("Centimeter (cm)", 1e-2),
                    "5": ("Decimeter (dm)", 1e-1),
                    "6": ("Meter (m)", 1),
                    "7": ("Decameter (dam)", 10),
                    "8": ("Hectometer (hm)", 100),
                    "9": ("Kilometer (km)", 1000),
                    "10": ("Thou / Mil", 0.0000254),
                    "11": ("Inch", 0.0254),
                    "12": ("Foot", 0.3048),
                    "13": ("Yard", 0.9144),
                    "14": ("Mile", 1609.344),
                    "15": ("League", 4828.032),
                    "16": ("Light-Day", 2.59020683712e13),
                    "17": ("Astronomical Unit", 1.495978707e11),
                    "18": ("Light-Year", 9.46073047258e15),
                    "19": ("Parsec", 3.08567758149e16)
                }

                while True:

                    print("\n" + "-" * 45)
                    print("        LENGTH CONVERSION")
                    print("-" * 45)

                    for key, value in units.items():
                        print(f"{key}. {value[0]}")

                    print("0. Back")

                    from_unit = input("\nConvert From: ")

                    if from_unit == "0":
                        break

                    if from_unit not in units:
                        print("Invalid choice!")
                        continue

                    to_unit = input("Convert To: ")

                    if to_unit == "0":
                        break

                    if to_unit not in units:
                        print("Invalid choice!")
                        continue

                    value = float(input("Enter value: "))

                    # Convert to meters
                    meters = value * units[from_unit][1]

                    # Convert from meters
                    result = meters / units[to_unit][1]

                    print(f"\n{value} {units[from_unit][0]}")
                    print(f"= {result} {units[to_unit][0]}")

            elif conv_choice == "2":
                print("Area Conversion - Coming Soon")

            elif conv_choice == "3":
                print("Volume Conversion - Coming Soon")

            elif conv_choice == "4":
                print("Mass Conversion - Coming Soon")

            elif conv_choice == "5":
                print("Speed Conversion - Coming Soon")

            elif conv_choice == "6":
                print("Time Conversion - Coming Soon")

            elif conv_choice == "7":
                print("Temperature Conversion - Coming Soon")

            elif conv_choice == "0":
                break

            else:
                print("Invalid choice!")

    elif choice == "4":
        print("Advanced Conversions - Coming Soon")

    elif choice == "5":
        print("Tables - Coming Soon")

    elif choice == "6":
        print("Perimeter Calculations - Coming Soon")

    elif choice == "7":
        print("Area Calculations - Coming Soon")

    elif choice == "8":
        print("Volume Calculations - Coming Soon")

    elif choice == "9":
        print("Angular Calculations - Coming Soon")

    elif choice == "10":
        print("Marks Calculations - Coming Soon")

    elif choice == "11":
        print("Economic Calculations - Coming Soon")

    elif choice == "12":
        print("SIP Calculations - Coming Soon")

    elif choice == "0":
        print("Thank you for using Not So Simple Calculator!")
        break

    else:
        print("Invalid choice! Please try again.")
