### sabsing
# October 10, 2021
#
# This is my Programming Assignment 3 where I made the game Mastermind with while loops, for loops, and if statements

legal_colors = ['R', 'G', 'B', 'Y', 'W', 'O', 'M', 'V']


def generate_color_sequence():
    import random
    random.seed()

    sequence = random.sample(range(len(legal_colors)), 4)
    return [legal_colors[i] for i in sequence]

colors = generate_color_sequence()

### You Code Here
print("Possible colors are", *legal_colors, sep=", ")
print("Please enter your guess with no spaces between colors. Colors cannot be repeated")

colors = list(colors)

guesses = 0
while guesses< 5:
    guesses+=1
    guess = input(f"Guess {guesses}: ").upper()
    guess = list(guess)
    if len(guess) > 4 or len(guess) < 4:
        print("Must have four color guesses, try again")
        guesses-=1
        continue
    else:
        guess_list = []
        for guess_letter in guess:
            if guess_letter not in legal_colors:
                print(f"{guess_letter} is not a valid color, try again")
                guesses-=1
                break
            elif guess_letter in guess_list:
                print("Colors cannot be repeated, try again")
                guesses-=1
                break
            else:
                guess_list += [f"{guess_letter}"]

        if guess[0] == colors[0]:
            output_1 = "R"
        elif guess[0] == colors[1] or guess[0] == colors[2] or guess[0] == colors[3]:
            output_1 = "W"
        else:
            output_1 = "_"
            
        if guess[1] == colors[1]:
            output_2 = "R"
        elif guess[1] == colors[0] or guess[1] == colors[2] or guess[1] == colors[3]:
            output_2 = "W"
        else:
            output_2 = "_"
            
        if guess[2] == colors[2]:
            output_3 = "R"
        elif guess[2] == colors[1] or guess[2] == colors[0] or guess[2] == colors[3]:
            output_3 = "W"
        else:
            output_3 = "_"
            
        if guess[3] == colors[3]:
            output_4 = "R"
        elif guess[3] == colors[1] or guess[3] == colors[2] or guess[3] == colors[0]:
            output_4 = "W"
        else:
            output_4 = "_"

        output=output_1 + output_2 + output_3 + output_4
        if output == "RRRR":
            print("You win!")
            break
        else:
            print(output)
            
    if guesses == 5 and output != "RRRR":
        print("You lose!")
        break


