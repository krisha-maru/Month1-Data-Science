def calculator():
    print('Simple calculator')
    while True:
        try:
            num1 = float(input('Enter first number:'))
            op = input('Enter operator (+,-,*,/)')
            num2 = float(input('Enter second number:'))

            if op == '+':
                print('Result:', num1+num2)
            elif op == '-':
                print('Result', num1-num2)
            elif op == '*':
                print('Result', num1*num2)
            elif op == '/':
                if num2 != 0:
                    print('Result', num1-num2)
                else:
                    print('Cannot divide by zero')
            else:
                print('Invalid operator')
        except ValueError:
            print('Invalid input')
        cont = input('Continue? (y/n):')
        if cont.lower() != 'y':
            break
calculator()


