def divide(num1, num2):
        return num1/num2

while True:
    try:
        print( divide(int(input()), int( input() ) ) )
        break
    except ZeroDivisionError:
        print('You can\'t divide by 0, try again!')
        continue
