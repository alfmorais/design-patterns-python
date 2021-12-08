class Calculator:

    def calculate(self, operation, num1, num2):
        if operation == "+":
            return self.__sum(num1, num2)
        elif operation == "-":
            return self.__subtract(num1, num2)
        else:
            print("Wrong operation!")

    def __sum(self, num1, num2):
        return num1 + num2

    def __subtract(self, num1, num2):
        return num1 - num2


calculator = Calculator()
results = calculator.calculate("+", 25, 25)
print(results)
results = calculator.calculate("-", 25, 25)
print(results)