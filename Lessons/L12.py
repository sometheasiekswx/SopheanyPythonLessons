for i in range(1, 100 + 1, 1):
    result = ''
    if i % 3 == 0:
        result = result + 'Fizz'
    if i % 5 == 0:
        result = result + 'Buzz'
    if i % 7 == 0:
        result = result + 'Tom'
    if i % 9 == 0:
        result = result + 'Scott'

    if result == '':
        print(i)
    else:
        print(result)
