"""
Filename: quiz2022.py
Author: Riddhimaan
Date: 8/07/2022
Description: This program is a general knowledge quiz, that will test the user's knowledge through various questions

"""

# dictionary used for predefined value of quiz questions
questions = {
    "1. What is the largest country by population in the world?: ": "A",
    "2. What year did the first world war end?: ": "B",
    "3. What is the most popular sport in the world?: ": "C",
    "4. What is arachnophobia the fear of?: ": "D",
    "5. How many dots appear on a dice?: ": "A",
    "6. In what country would you find Mount Kilimanjaro?: ": "C",
    "7. What is the worlds fastest bird?: ": "D",
    "8. Which Football team does Messi play for?: ": "B",
    "9. How many days in a leap year?: ": "B",
    "10. Whats the largest ocean?: ": "A",
    "11. How many teeth does an adult human have?: ": "D"
}

# 2d list used for predefined value of quiz answers
options = [["A. China", "B. Russia", "C. India", "D. United States"],
           ["A. 1945", "B. 1918", "C. 1916", "D. 1917"],
           ["A. Cricket", "B. Basketball", "C. Football", "D. Rugby"],
           ["A. Insects", "B. Frogs", "C. Snakes", "D. Spiders"],
           ["A. 21", "B. 36", "C. 32", "D. 30"],
           ["A. Zimbabwe", "B. Africa", "C. Tanzania", "D. Kenya"],
           ["A. Red Hawk", "B. Seagull", "C. Bald Eagle", "D. Peregrine Falcon"],
           ["A. Barcelona", "B. PSG", "C. Real Madrid", "D. Arsenal"],
           ["A. 365", "B. 366", "C. 364", "D. 367"],
           ["A. Pacific Ocean", "B. Atlantic Ocean", "C. Indian Ocean", "D. East Blue"],
           ["A. 36", "B. 34", "C. 30", "D. 32"]]


# --------------------Starting a New game for the user-----------------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("--------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)

        guess = input("Enter (A,B,C or D): ")
        guess = guess.upper()

        # call validate_guess method to validate the user guesses
        guess = validate_guess(guess)

        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)
    play_again()


# ----------Validated user guess--------------------------
def validate_guess(option):
    user_guess = option
    check = True
    while check:
        if user_guess == "A" or user_guess == "B" or user_guess == "C" or user_guess == "D":
            check = False
        else:
            print("INVALID INPUT")
            user_guess = input("Please enter a valid option (A,B,C or D): ").upper()

    return user_guess


# --------------Check whether the user guess is correct or not!------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0


# -------------------------------------------------------
def display_score(correct_guesses, guesses):
    print("--------------------------")
    print("RESULTS")
    print("--------------------------")

    print("ANSWERS: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("GUESSES: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses / len(questions)) * 100)
    print("Your score is: " + str(score) + "%")


# --------------------------------------------
def play_again():
    print()
    print("Do you want to play the quiz again? Enter 'yes' to play, 'rules' to see rules or any other key to leave")
    play_game = input("Enter: ")

    play_game = play_game.lower()

    if play_game == "yes":
        new_game()

    elif play_game == "rules":
        display_rules()


# ---------------------------------------------
def display_rules():
    print()
    print("===RULES===")
    print()
    print("In this quiz there will be 11 multichoice questions based on general knowledge")
    print("You will have to enter A,B,C or D depending what you think is the answer")
    print("After each question it would be displayed if you got the question right or not")
    print("At the end of the quiz, your score and answers would be displayed")
    print()

    print("Do you want to play the quiz now? Enter 'yes' to play, 'rules' to see rules or any other key to leave")
    play_game = input("Enter: ")

    play_game = play_game.lower()

    if play_game == "yes":
        new_game()

    elif play_game == "rules":
        display_rules()


# ----------------------------------------------

def main():
    # Start of program menu to allow user to start or stop the quiz
    print("~~General Knowledge Quiz~~")
    print("=====================")
    print()

    print()
    print("===MENU===")
    print("A) Enter 'yes' to start the quiz")
    print("B) Enter 'rules' to see the rules of the quiz")
    print("C) enter any other key to leave")

    # input function for user to decide if they want to play or not
    play_game = input("Enter: ")

    # turning the input from user to all caps (YeS/YES/yEs --> yes)
    play_game = play_game.lower()

    # if user entered yes, the quiz starts
    if play_game == 'yes':
        new_game()

    elif play_game == "rules":
        display_rules()

    print("Thanks for trying me! Goodbye")


main()
