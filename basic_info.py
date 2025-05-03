def basic_info():
    name, prof = input('Hey, what is your name and profession? (Reply with "," separator)\n').split(',')
    exp = input('Okay, how long do you work in QA field? (Reply in years, exmpl: 0.6)\n')
    print(f'Hey {name}, looks like you work as {prof} with {exp} years of experience!')
    quiz_reply = input('Little quiz: what is variable in python?\n')
    if 'name' in quiz_reply or 'names' in quiz_reply or 'placeholder' in quiz_reply:
        print('You\'re correct!')
    else:
        print('Not exactly.')

basic_info()