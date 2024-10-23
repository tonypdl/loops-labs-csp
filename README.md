# loops-labs-csp
# AP CSP Loops Labs Practice

## Lab #1

Write a function `reverse_number()` that takes in an integer and returns a string. This string will be the original integer but in reverse order. You must use a loop and modulus to perform the reverse.

Examples:
- `reverse_number(234)` returns `"432"`
- `reverse_number(10000)` returns `"00001"`

## Lab #2

Write a function named `digit_adder()`. This function will take in an integer as a parameter and return the sum of the digits of the integer. You must use a loop and modulus to perform the addition of the digits.

Examples:
- `digit_adder(123)` returns `"6 is the sum of the digits of 123"`
- `digit_adder(9005)` returns `"14 is the sum of the digits of 9005"`

## Lab #3

Write a function named `divisor_finder()`. This function takes an integer parameter and returns a string listing the number’s proper divisors. Use modulus to find the divisors.

Examples:
- `divisor_finder(6)` returns `"6 has the divisors 1 2 3"`
- `divisor_finder(45)` returns `"45 has the divisors 1 3 5 9 15"`

## Lab #4

A perfect number is any number that is equal to the sum of its divisors. Write a function that takes an integer parameter and returns `True` if the number is perfect and `False` otherwise. Use mod (%) to find divisors. Name this function `perfect_number()`.

Examples:
- `perfect_number(6)` returns `True`
- `perfect_number(45)` returns `False`
- `perfect_number(14)` returns `False`
- `perfect_number(8128)` returns `True`
- `perfect_number(33550336)` returns `True`

Call the function three times to test if it works properly. Example:
```python
print(perfect_number(6))  # should return True
```

## Lab #5

Write a function that takes a string and a target character and returns a string with all instances of the target character removed. Do not use any Python/programming shortcuts. Name this function `letter_remover()`.

Examples:
- `letter_remover("abba babies", "b")` returns `"aa aies"`
- `letter_remover("Sam ate aardvark", "a")` returns `"Sm te rdvrk"`

Call the function three times to test if it works properly. Example:
```python
print(letter_remover("abba babies", "b"))  # should return "aa aies"
```

## Lab #6 - Mini-Coding Project

### Mini-Coding Project: Loops

**Objective:**

Create a simple number guessing game where the user has to guess a randomly generated number between 1 and 100. The game will provide feedback if the guess is too high or too low, and it will continue until the user guesses the correct number.

**Steps:**

1. **Generate a Random Number:**
    - Use the `random` module to generate a random number between 1 and 100.

2. **Prompt the User for a Guess:**
    - Use a `while` loop to repeatedly ask the user for their guess until they guess correctly.

3. **Provide Feedback:**
    - If the guess is too high, inform the user.
    - If the guess is too low, inform the user.
    - If the guess is correct, congratulate the user and end the game.

4. **Keep Track of Attempts:**
    - Count the number of attempts the user makes and display it when they guess correctly.

**Pseudocode (Natural Language Walkthrough):**

- Import the `random` module.
- Generate a random number between 1 and 100.
- Initialize a variable to count the number of attempts.
- Use a `while` loop to repeatedly ask the user for their guess.
  - Inside the loop:
     - Get the user's guess.
     - Compare the guess to the random number.
     - Provide feedback if the guess is too high, too low, or correct.
     - Increment the attempt counter.
- When the user guesses correctly, exit the loop and display the number of attempts.

**Helpful Hints and Explanation:**

- The `random.randint(x, y)` function generates a random number between `x` and `y` (inclusive). Remember to `import random` at the top of your program to have access to random functions.
- A `while True` loop continues indefinitely until the user guesses the correct number.
- The `input` function can be used to get the user's guess, which is then converted to an integer.
- The program provides feedback based on the user's guess and keeps track of the number of attempts.
- You can use a function for the entire game if you want to. You do not have to use a function if the program can work without one.
- When the user guesses correctly, if using it, the `while True` loop breaks, and the program congratulates the user and displays the number of attempts.
