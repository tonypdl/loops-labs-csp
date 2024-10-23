"""
Lab #6 - Mini-Coding Project
Mini-Coding Project: Loops
Objective:

Create a simple number guessing game where the user has to guess a randomly generated number between 1 and 100. The game will provide feedback if the guess is too high or too low, and it will continue until the user guesses the correct number.

Steps:

Generate a Random Number:

Use the random module to generate a random number between 1 and 100.
Prompt the User for a Guess:

Use a while loop to repeatedly ask the user for their guess until they guess correctly.
Provide Feedback:

If the guess is too high, inform the user.
If the guess is too low, inform the user.
If the guess is correct, congratulate the user and end the game.
Keep Track of Attempts:

Count the number of attempts the user makes and display it when they guess correctly.
Pseudocode (Natural Language Walkthrough):

Import the random module.
Generate a random number between 1 and 100.
Initialize a variable to count the number of attempts.
Use a while loop to repeatedly ask the user for their guess.
Inside the loop:
Get the user's guess.
Compare the guess to the random number.
Provide feedback if the guess is too high, too low, or correct.
Increment the attempt counter.
When the user guesses correctly, exit the loop and display the number of attempts.
Helpful Hints and Explanation:

The random.randint(x, y) function generates a random number between x and y (inclusive). Remember to import random at the top of your program to have access to random functions.
A while True loop continues indefinitely until the user guesses the correct number.
The input function can be used to get the user's guess, which is then converted to an integer.
The program provides feedback based on the user's guess and keeps track of the number of attempts.
You can use a function for the entire game if you want to. You do not have to use a function if the program can work without one.
When the user guesses correctly, if using it, the while True loop breaks, and the program congratulates the user and displays the number of attempts.
"""

#CODE
#BELOW
#HERE

