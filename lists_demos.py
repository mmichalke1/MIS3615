a=[20, 30, 'joe', True]
print(a[2])

AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']

print(AFC_east[0])

AFC_east[3] = 'New York Giants'
print(AFC_east)

# s = 'Shankar'
# s[0]= 'T' This will not work because strings don't support this
# print(s)

print('Miami' in AFC_east)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[1][2][0]) #how to call ruby, a string within a list within a list within a list

for team in AFC_east:
    print(team)

print(len(AFC_east))
print(len(AFC_east[0]))

#find total number of characters in a list
s = 0
for team in AFC_east:
    print(team, len(team))
    s += len(team)
print(s)

squares = []

for n in range(1,10):
    squares.append(n**2)

print(squares)

numbers = [7,10,69,652542]
for number in numbers:
    numbers[numbers.index(number)] = number**2
print(numbers)

numbers.remove(49)
print(numbers)

team = 'New England Patriots has a lot of great players'
words = team.split()

print(words)
print(len(words))

s = 'spam-spam-spam'
t = s.split('-')  #splits where ever you determine, default is a space(' ')
print(t)

new_sentence = ' '.join(words)
print(new_sentence)

name = 'Shankar'
d = list(name) #puts every character from name into a list
print(d)
print(''.join(d))
