import random

def opening_print():
    print("""I am thinking of a 3-digit number. Try to guess what it is.
    Here are some clues:
    When I say:  That means:
    Pico         One digit is correct but in the wrong position.
    Fermi        One digit is correct and in the right position.
    Bagels       No digit is correct.
    """)


def generate_numbers():
    print("I have thought of a number.")
    numbers = []

    while len(numbers) < 3:
        random_number = random.randint(1, 9)
        if str(random_number) not in numbers:
            numbers.append(str(random_number))
        else:
            pass
    
    # return "".join(numbers)
        return "123"


# print(generate_numbers())

def get_user_input() -> str:
    prompt = input("Please make a guess: \n").strip()
    if prompt.isnumeric() and len(prompt) == 3:
        return prompt
    else:
        print("Invalid input")
        return get_user_input()


def check_positions(numbers, guess):
    progress = []
    for x in range(3):
        if numbers[x] == guess[x]:
            progress.append("Fermi")
        elif  numbers[x] in guess:
            progress.append("Pico")
    
    if progress == []:
        return "Bagels"
    else:
        return (" ".join(progress)).strip()



def check_win(positions) -> bool:
    if positions == "Fermi Fermi Fermi":
        return True
    else:
        return False


def guess_left(remaining_guesses) -> int:
   remaining_guesses -= 1
   return remaining_guesses


def replay() -> bool:
    prompt = input("Would you like to play again? [Y/n]: \n")

    if prompt.isalpha() and prompt.upper() == "Y":
        return True
    elif prompt.isalpha() and prompt.upper() == "N":
        print("Thank you for playing!")
        return False
    else:
        print("Please enter either 'Y' or 'n'")
        return replay()
    
def game_on(remaining_guesses, numbers) -> bool:
    if remaining_guesses > 0:
        return True
    else:
        print(f"You didn't get it. The correct answer was {numbers}")
        return False


def run_game():
    remaining_guesses = 3
    opening_print()
    numbers = generate_numbers()
    play = game_on(remaining_guesses, numbers)
    while play:
        user_guess = get_user_input()
        positions = check_positions(numbers, user_guess)
        result = check_win(positions)
        print(result)
        if result == True:
            print(f"You got it!")
            break
        elif result == False:
            remaining_guesses = guess_left(remaining_guesses)
            print(positions)
            if remaining_guesses == 1:
                print(f"You have {remaining_guesses} guess left.")
            else:
                print(f"You have {remaining_guesses} guesses left.")
        play = game_on(remaining_guesses, numbers)
    
    another_round = replay()
    if another_round:
        run_game()


        
    
if __name__ == "__main__":
    run_game()