# The user's inputs for the numbers and the operators
num1 = float(input('Enter your first number: '))
Operator = input('Enter operator: ')
num2 = float(input('Enter your second number: '))

# if Operator is (+ | - | * | /) then  print out number 1 (+ | - | * | /) number 2
if Operator == '+':
    print(num1 + num2)
elif Operator == '-':
    print(num1 - num2)
elif Operator == '/':
    print(num1 / num2)
elif Operator == '*':
    print(num1 * num2)

# if the user didn't put an operator
else:
    print('Not a valid operator')
