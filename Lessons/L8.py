success = False
user_input = 0

# try: user_input = int(input('Please enter a number: ')) success == True

while success == False:
    try:
        user_input = int(input('Please enter a number: '))
        success = True

    except:
        print('Try again')

print(user_input)
