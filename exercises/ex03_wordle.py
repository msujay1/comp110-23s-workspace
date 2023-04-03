"""EX03 Wordle Game."""

__author__ = "730556908"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(word:str,single_charecter:str) -> bool:
    """When looking at two strings, return True if a single charecter is found in any index of the first string and flase otherwise. """
    assert len(single_charecter) == 1
    i: int = 0
    while i < len(word):
        if single_charecter == word[i]:
            return(True)
        else:
            i = i + 1
    return(False)

def emojified(guess:str,secret:str) -> str:
    """Will check correct emoji on each index. """
    assert len(guess) == len(secret)
    string_emoji: str = ""
    i: int = 0
    while i < len(secret):
        if contains_char(secret, guess[i]) is True and guess[i] != secret[i]:
            string_emoji = string_emoji + YELLOW_BOX
        if contains_char(secret, guess[i]) is True and guess[i] == secret[i]:
            string_emoji = string_emoji + GREEN_BOX
        if contains_char(secret, guess[i]) is False:
            string_emoji = string_emoji + WHITE_BOX
        i += 1
    return string_emoji

def input_guess(length_expected:int) -> str:
    """Will allow user to guess based on the secret words count."""
    user_input: str = input(f"Enter a {length_expected} character word: ")
    while len(user_input) != length_expected:
        user_input = input(f"That wasn't {length_expected} chars! Try again: ")
    return user_input

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    guess: str = " "
    counter : int = 1
    while guess != secret:
        print(f"====Turn {counter}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if counter <= 6 and guess != secret:
            counter += 1
        if counter >= 1 and guess == secret:
            print(f"You won in {counter}/6 turns!")
        if counter == 7:
            print("X/6 - Sorry, try agin tomorrow!")
            guess = secret

if __name__ == "__main__":
    main()

