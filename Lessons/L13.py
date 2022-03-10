rules = {3: 'Fizz', 5: 'Buzz'}
for i in range(1, 101):
    output = ''.join(key_value for val,
                     key_value in rules.items() if i % val == 0)
    print(output or i)


for i in range(1, 10):
    if i > 5:
        print(i)

[print(i) for i in range(1, 10) if i > 5]
