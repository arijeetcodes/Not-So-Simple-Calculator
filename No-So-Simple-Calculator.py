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
        print("Advanced Arithmetics - Coming Soon")

    elif choice == "3":
        print("Basic Conversions - Coming Soon")

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
