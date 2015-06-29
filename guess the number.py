# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import math
import random

# initialise the global variables
secret_number = 1
guesses_remaining = 7
num_range = 100

def input_guess(guess):
    global guesses_remaining
    num = int(guess)
    print "Guess was", guess
    
    # decrement the number of guesses remaining
    guesses_remaining -= 1
    print "Number of remaining guesses is", guesses_remaining
    
    # check if entered number is correct, higher or lower
    if secret_number == num:
        print "Correct!\nStarting a new game.\n"
        new_game()
    elif guesses_remaining == 0:
        print "You ran out of guesses. The number was", secret_number, "\n"
        print "Starting a new game.\n"
        new_game()
    elif secret_number > num:
        print "Go Higher!\n" 
    elif secret_number < num:
        print "Go Lower!\n"

# set the range to [0, 100) and restart the game        
def range100():
    global num_range, guesses_remaining
    num_range = 100
    guesses_remaining = 7
    new_game()

# set the range to [0, 1000) and restart the game
def range1000():
    global num_range, guesses_remaining
    num_range = 1000
    guesses_remaining = 10
    new_game()

# helper function to start and restart the game
def new_game():
    global secret_number, guesses_remaining
    if num_range == 100:
        guesses_remaining = 7
    else:
        guesses_remaining = 10
    print "New game. Range is from [0, %d)" % num_range
    print "Number of remaining guesses is", guesses_remaining
    print ""
    secret_number = random.randrange(0,num_range)

# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

# call new_game 
f.start()
new_game()

# always remember to check your completed program against the grading rubric
