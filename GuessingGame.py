import random


def difficulty_level():
    print("""
Welcome
You can choose a difficulty level you desire by typing your preference between EASY, MEDIUM or HARD.
""")
    level_choice = input("Please type a level").upper()
    return level_choice


def wrong_guess(guess, random_num, max_guess_count, guess_count):
    if guess != random_num:
        print("You are wrong!")
        guess_left = max_guess_count - guess_count
        print(f" You have {guess_left} guesses left")
        if guess_left == 0:
            print("Game Over")


status = True
get_level = difficulty_level()
while status:
    guess_count = 0

    if get_level == "EASY":
        print("Guess a number between 1-10. You get 6 guesses!")
        max_guess_count = 6
        while guess_count < max_guess_count:
            random_num = random.randint(1, 10)
            try:
                guess = int(input("Guess?"))
                guess_count += 1
                if guess == random_num:
                    print("Congratulations, you got it right!")
                    status = False
                    break
                else:
                    wrong_guess(guess, random_num, max_guess_count, guess_count)
                    status = False
            except ValueError:
                print("Invalid Guess. Make Another.")

    elif get_level == "MEDIUM":
        print("Guess a number between 1-20. You get 4 guesses!")
        max_guess_count = 4
        while guess_count < max_guess_count:
            random_num = random.randint(1, 20)
            try:
                guess = int(input("Guess?"))
                guess_count += 1
                if guess == random_num:
                    print("Congratulations, you got it right!")
                    status = False
                    break
                else:
                    wrong_guess(guess, random_num, max_guess_count, guess_count)
                    status = False
            except ValueError:
                print("Invalid Guess. Make Another.")

    elif get_level == "HARD":
        print("Guess a number between 1-50. You get 3 guesses!")
        max_guess_count = 3
        while guess_count < max_guess_count:
            random_num = random.randint(1, 50)
            try:
                guess = int(input("Guess?"))
                guess_count += 1
                if guess == random_num:
                    print("Congratulations, you got it right!")
                    status = False
                    break
                else:
                    wrong_guess(guess, random_num, max_guess_count, guess_count)
                    status = False
            except ValueError:
                print("Invalid Guess. Make Another.")

    else:
        get_level = input("Choose a valid difficulty level").upper()











