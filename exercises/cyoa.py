"""EX06 CYOA."""
import random


__author__ = "730556908"

points: int = 0
player: str = ""
emoji: str = "\U0001F61C"


def main() -> None:
    """Main part of the program."""
    greet()

    user_wants_to_exit: bool = False
    
    while user_wants_to_exit is False:
        # ask user to choose betweeen 3 options
        user_choice = int(input("Enter 1 for a coin flip game, Enter 2 for a price guess game or Enter 3 to exit the game: "))
        if user_choice == 1:
            coinflip()
        if user_choice == 2:
            priceguess(points)
        if user_choice == 3:
            user_wants_to_exit = True
            exit(input("Thank You for playing!" + emoji))

   
def greet() -> None:
    """This function will print a message for the player asking for his name and context of the game."""
    global player
    greeting: str = input("Welcome to the best game in the world. Please enter your name :")
    player = greeting
    print(f'Hello {player}')


def coinflip() -> None:
    """This procedure has the user guess whether it will be heads or tails and if they get it right they will receive 3 points."""
    global points
    guess1: str = input("This game requires you to guess either heads or tails. You will receive 3 points if the answer is right. What is your guess? ")

    generate_random: int = random.randint(0, 1)   # 0 = tails, 1 = heads

    users_guess_as_int: int

    if guess1 == "tails":
        users_guess_as_int = 0
    if guess1 == "heads":
        users_guess_as_int = 1

    if users_guess_as_int == generate_random:
        print("That is correct! You recieve 3 points.")
        points += 3
    else: 
        print("That is incorrect. Try again!")
      

def priceguess(guess_int: int) -> int:
    """This function asks the user to guess the price of an object."""
    price: int = 110
    index: int = 0
    score: int = 0
    while index < 3:
        guess_int: int = int(input("What is the price of white Air Force 1's? "))
        if guess_int == price:
            print("Congratulations, you have earned 3 more points!")
            score += 3
            return
        else:  
            guess_int = input("Sorry that is incorrect. You have more guesses!")
            guess_int = input("What is your new guess?")
            index += 1
    return score


if __name__ == "__main__":
    main()
