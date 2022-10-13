numbers = [2, 56, 85, 55, 95, 52, 12]

sum = 0

for val in numbers:
    sum = sum + val

print(sum)

# for i in range(10):
#     print(i)

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print('????')

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

print(range(10))
print(list(range(10)))

# program to display student's marks from record
student_name = 'Jack'

marks = {'James': 90, 'Jules': 55, 'Arthur': 77}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('No entry with that name found.')
