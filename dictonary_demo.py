grades = {}

grades['Shankar'] = 59
grades['Johnathan'] = 99
grades['Alvie'] = 80
grades['Lauren'] = 90

print(grades)
print(grades['Johnathan'])

grades['Alvie'] = 85

print(grades)

for name in grades:
    grades[name] += 1

print(grades)
print(len(grades))
print('Shankar' in grades)

for score in grades.values():
    score += 1
    print(score)

print(grades.values())

for name, score in grades.items():
    print(name, ':', score)
