class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

def main():
    calc = Calculator()
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            break

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"The result is: {calc.add(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {calc.subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {calc.multiply(num1, num2)}")
            elif choice == '4':
                try:
                    print(f"The result is: {calc.divide(num1, num2)}")
                except ValueError as e:
                    print(e)
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
