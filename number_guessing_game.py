import random

#asks user for lower limit number and higher limit number (Returns string or 2 int values)
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

