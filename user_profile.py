
def user_profile():
    while True:
        name = input('Hey, what\'s your name?\n')
        if name:
            print(f'Nice to meet you {name}')
        else:
            print(f'Oops.. Looks like you didn\'t type your name, try again please')
            continue
        prof = input('What is your profession?\n')
        if prof:
            print(f'You work as {prof}')
        else:
            print(f'Oops.. Looks like you didn\'t type your profession, try again please')
            continue
        instrument = input('What is your favorite instrument?\n')
        if instrument:
            print(f'Your prefer {instrument}, nice choice!')
        else:
            print(f'Oops.. Looks like you didn\'t type your instrument, try again please')
            continue
        break

user_profile()