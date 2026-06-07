# guessing-game
This is my first python project where the user must try to guess a random number set by the computer. The random number sits within a set range that is decided by the user. The user wins once they guess the number correctly then the program ends.

Uses the random library for random number selection
```python
import random
```

The get_range function asks the user set the lower and higher bound numbers. The function returns a string if the bounds are invalid (lower bound is bigger than higher bound) or 2 int values (lower bound, higher bound) 
```python
def get_range():
    num1 = input("Write a number to set as the lower limit\n")
    while num1.isdigit()==False:
            print("\nThis is not a integer!\n")
            num1 = input("Select a new number!\n")
            if num1.isdigit() == True:
                num1 = int(num1)
                break
    num1 = int(num1)    
    num2 = input("Write a number to set as the higher limit\n")
    while num2.isdigit()==False:
        print("\nThis is not a integer!\n")
        num2 = input("Select a new number!\n")
        if num2.isdigit() == True:
            num2 = int(num2)
            break
    num2 = int(num2)     
    if num1>num2:
        return "Invalid Range"
    else:
        num_lim = {
            "Low": num1,
            "High": num2
        }
        return num_lim
```

The get_guess function gets a user input to use as a guess for the random number. It also makes sure that the user inputs a valid number and casts the input as an int value.
```python
def get_guess(low_lim,high_lim):
    guess = input()
    while guess.isdigit()==False:
            print("\nThis is not a integer!\n")
            guess = input("Select a new number!\n")
            if guess.isdigit() == True:
                guess = int(guess)
                break
    guess = int(guess)
    return guess
```

This is the main code that calls all the functions and their returned values to use for the game itself.
```python
game_limits = {}

#determines if user continues or re-enters new values
result = get_range()
while result == "Invalid Range":
    print("\nInvalid Range: Lower limit must be less than Higher limit!\n")
    result = get_range()

game_limits = result

#gets random int within the range set by user
random_num = random.randint(game_limits["Low"], game_limits["High"])

print("\nGame Limits Confirmed.")
print(f"Lower Limit: {game_limits['Low']}")
print(f"Higher Limit: {game_limits['High']}")

#asks user to guess the random number
print(f"\nGuess a number between {game_limits['Low']} and {game_limits['High']}\n")
user_guess = get_guess(game_limits['Low'],game_limits["High"])

#if user guesses wrong, try again until correct
while user_guess != random_num:
    if user_guess > random_num:
        print("\nToo high, Try Again!\n")
        user_guess = get_guess(game_limits['Low'],game_limits["High"])
    elif user_guess < random_num:
        print("\nToo low, Try Again!")
        user_guess = get_guess(game_limits['Low'],game_limits["High"])
    elif user_guess == random_num:
        break

print(f"\nYou Win! The number was {random_num}!")
```
