### 1

grams = 12345

def get_kg_weight(weight):
    kgs = int(round(weight / 1000, 0))
    print(f'{weight} grams contains {kgs} full kgs')

get_kg_weight(grams)

### 2

number = 1234

def get_last_char(num):
    last_digit = list(str(num))[-1]
    print(f'Last digit in number {num} is {last_digit}')

get_last_char(number)

### 3

number_1 = 14
number_2 = -4
number_3 = 15

def positive_and_even(num):
    if num > 0 and num % 2 == 0:
        print(f'{num} is positive and even')
    else:
        print(f'{num} failed one of states')

positive_and_even(number_1)
positive_and_even(number_2)
positive_and_even(number_3)

### 4

num_1 = 150
num_2 = 99
num_3 = 0
num_4 = 100

def in_range(num):
    if num >= 0 and num < 101: # if num in range(101): #
        print(f'{num} in range')
    else:
        print(f'{num} not in range')

in_range(num_1)
in_range(num_2)
in_range(num_3)
in_range(num_4)

### 5

sample_1 = 9
sample_2 = 10

def not_multiple_3(num):
    if num % 3 == 0:
        print(f'{num} is multiple of 3')
    else:
        print(f'{num} is not multiple of 3')

not_multiple_3(sample_1)
not_multiple_3(sample_2)