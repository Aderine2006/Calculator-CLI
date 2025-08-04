# calculator.py
#declared an addition function with two input parameteres for adding two numbers
def add(x, y):
    return x + y
#Declared an subtraction function with two input parameteres for subtracting two numbers
def subtract(x, y):
    return x - y
#Declared an multiplication function with two input parameteres for multiplying two numbers
def multiply(x, y):
    return x * y
#declared an division function with two input parameteres for dividing two numbers
def divide(x, y):
#checking whether y is equal to zero ,because dividing by zero will result in infinity
    if y == 0:
#displaying the error message
        return "Error! Division by zero."
    return x / y
#declaring a main function that welcomes the user to use the CLI Calculator 
def main():
    print("Welcome to CLI Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
#Ask's the user of what operation has to be performed
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        try:
#Asking the user to enter the two parameters that has to be performed for operation
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
        except ValueError:
#pops invalid output! if the user enters other than what expected
            print("Invalid input! Please enter a number.")
    else:
        print("Invalid choice!")
#calling the main function to execute the code for calculation
if __name__ == "__main__":
    main()
#Hope you understand the code 
