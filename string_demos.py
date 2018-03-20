team = 'New England Patriots'

first_letter = team[0]
print(first_letter)
print(team[4])
print(len(team))

print(team[-20]) #think of this as team[20-20=0]

print(team[-8:]) #slicing the string

print(team[::-1])

new_team = team[:12] + 'Yankees'
print(new_team)

prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)

for i in 'Matthew':
    print(i, ord(i))

name = 'Matthew Michalke'
vowel = 0
consonant = 0
space = 0
for letter in name:
    if letter in 'aeiouAEOIU':
        vowel += 1
    elif letter in ' ':
        space += 1
    else:
        consonant +=1


print(vowel, consonant, space)

print('e' in team)

print(team.lower())
c = 'babson college'
print(c.title())

s = 'abababababacd'
print(s.count('ab'))

print(c.isupper())
