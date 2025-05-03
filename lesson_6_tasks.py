### 1

numbers = [1, 2, 3]
numbers.append(4)
print(numbers)

### 2

fruits = ['Moscow', 'London', 'Oslo']
del fruits[0]
fruits.remove('London')
print(fruits)

### 3

cities = ['Kyiv', 'Paris', 'Dubai', 'Washington']
print(cities[2])

### 4

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[3:7])

### 5

colors = ["red", "green", "blue"]
colors[1] = 'yellow'
print(colors)

### 6

animals = ["cat", "dog", "rabbit", "hamster"]
print(len(animals))

### 7

student = {"name": "Ivan", "age": 20}
student.update({'grade': 'A'})
print(student)

### 8

student = {"name": "Ivan", "age": 20, "grade": "B"}
student['grade'] = 'A'
print(student)

### 9

student = {"name": "Ivan", "age": 20, "grade": "A"}
del student['age']
print(student)

### 10

student = {"name": "Ivan", "age": 20, "grade": "A"}
print(f'Name of student is {student['name']}')

### 11

student = {"name": "Ivan", "age": 20, "grade": "A"}

def key_exists(key, dict_sample: dict):
    if key in dict_sample.keys():
        print(f'Key "{key}" was found in {dict_sample}')
    else:
        print(f'Key "{key}" was not found in {dict_sample}')

key_exists('grade', student)

### 12

student = { "name": "Ivan", "address": { "city": "Moscow", "street": "Lenina" } }
student['address']['city'] = 'Oslo'

print(student)


### 13

student = { "name": "Maria", "grades": [75, 82, 90] }
student['grades'][0] = 85
print(student)

### 14

students = [ {"name": "Ivan", "age": 20}, {"name": "Petya", "age": 22} ]
students[1]['age'] = 23
print(students)

### 15

colors = ("red", "green", "blue")
print(f'Green present in colors: {'green' in colors}. Tuple length: {len(colors)}')