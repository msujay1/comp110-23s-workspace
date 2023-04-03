"""EX02 - One Shot Wordle Game """

__author__ = "730556908"

SECRET: str = "python"
guess: str = input(f"What is your {len(SECRET)}- letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
yellowbool: bool = False
i: int = 0
x : int = 0
output: str = ""

# here i checked the length of guess and the length of secret and if the guess was wrong number of charecters, the old guess became the new guess
while len(guess) != len(SECRET):
     newguess: str = input(f"That was not {len(SECRET)} letters! Try again: ")
     guess = newguess

# here the conditions are printing either a green box, yellow box or white box based on a word guess
while i < len(SECRET):
    if guess[i] == SECRET[i]:
        output = output + GREEN_BOX
    else:
        yellowbool = False
        x = 0
        while yellowbool is not True and x < len(SECRET):
            if guess[i] == SECRET[x]:
                yellowbool = True
            else:
                x = x + 1
        if yellowbool is True:   
            output = output + YELLOW_BOX
        else:
            output = output + WHITE_BOX
    i = i + 1

# here the output is brinted based on if the guess which is 6 letters is the 'python' or not
print(output)

if(guess != SECRET): 
    print("Not quite. Play again soon!")
else: 
    print("Woo! You got it!")
