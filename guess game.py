import random
# create code to greet the player
name = input("Hello, what is your name?")
x = int(input('How many numbers should we use?'))
greeting = "Okay {}, I'm thinking of a number of 1 to {}." .format(name, x)
print(greeting)

#created game as a function so you can play multiple times
def game(x):
    people_num = 0 #create the variable that will store the players guess
    i = 0 #create variable that keeps track of how many guess you have
    n = 0 #create flag variable. This one will only change if you guess right or break the game.
    comp_num = random.randint(1, x) #this is the computer's random guess
    #print(comp_num)  #this can be uncommented while checking to make sure the code works
    while i < 5: #you will stay in this while loop as long as your i(# of guesses) isn't above 5
        people_num = input("Take a guess: ") #player takes their guess
        i = i+1 #adds 1 to the i after every player guess
        if people_num.isdigit() and int(people_num) <=x and int(people_num) > 0: #checks to make sure the guess is within 1-1000 and not a letter
            if int(people_num) == comp_num: #this "if,elif,else" sees how the guess is compaired to the computers
                n = n+1 #adds 1 to the flag so you don't get the disappointing message
                print('Good job, {}! You guessed my number in {} guess(es)!' .format(name, i))
                break #breaks you out of while loop
            elif int(people_num) > comp_num:
                print('Your guess is too high.')
            else:
                print('Your guess is too low.')
            print('You have ' + str(5-i) + " guess(es) left!\n") #after it runs through the loops it tells you how many guesses you have
        else:
            n = n+2 #if it didn't pass the first if because you broke the rules a 2 is added to the flag
            break #breaks you out of the while loop cause you broke the rules
    if n == 0: #if you didn't win or broke the rules, this is where you end up
        print("\nOhh you suck, better luck next time!")
        print('My number was {}' .format(comp_num))
    elif n == 2: #if you did break the rules you get this message.
        print("The rules were very clear. You're no longer allowed to guess.")

#as long as the player types 'yes' after the game, they can start new games
play_again = 'yes'
while play_again.lower() == 'yes':
    game(x)
    play_again = input('\nWould you like to play again?\n')

print('Have a good day!')
