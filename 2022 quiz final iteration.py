"""
Filename: QUIZ_2022_Python_Assesment_Final.py
Author: Riddhimaan Banerjee
Date: 8/07/2022
Description: This program is a general knowledge quiz,
that will test the user's knowledge through various questions

"""
import time

# dictionary used for predefined values of quiz questions
# here keys are questions and values are the actual answer
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

# 2d list used for predefined value of quiz options
options = [["A. China", "B. Russia", "C. India", "D. United States"],
           ["A. 1945", "B. 1918", "C. 1916", "D. 1917"],
           ["A. Cricket", "B. Basketball", "C. Football", "D. Rugby"],
           ["A. Insects", "B. Frogs", "C. Snakes", "D. Spiders"],
           ["A. 21", "B. 36", "C. 32", "D. 30"],
           ["A. Zimbabwe", "B. Africa", "C. Tanzania", "D. Kenya"],
           ["A. Red Hawk", "B. Seagull",
            "C. Bald Eagle", "D. Peregrine Falcon"],
           ["A. Barcelona", "B. PSG", "C. Real Madrid", "D. Arsenal"],
           ["A. 365", "B. 366", "C. 364", "D. 367"],
           ["A. Pacific Ocean", "B. Atlantic Ocean",
            "C. Indian Ocean", "D. East Blue"],
           ["A. 36", "B. 34", "C. 30", "D. 32"]]

user_name = ""

# ---main method to call all other methods---


def main():
    # Start with program menu to allow user to start or stop the quiz
    print("***********************************")
    print("~~General Knowledge Quiz 2022~~")
    print("***********************************")
    print()

    print()
    print("===MENU===")

    # calling the function of the menu
    menu_functionality()

    print("Thanks for trying the quiz!! Goodbye")

# -----menu_functionality method to contain the user's choice-----


def menu_functionality():

    # printing the options the user can do
    print("Do you want to play the quiz?")
    print("A) Enter 'A' to start the normal quiz")
    print("B) Enter 'B' to start the hard quiz")
    print("C) Enter 'C' to see the rules of the quiz")
    print("D) enter any other key to leave")

    user_choice = input("Enter your choice : ").strip()

    # turning the input from user to lower case
    play_game = user_choice.lower()

    # if user entered 'a',start the quiz but set the marking feature to normal
    if play_game == 'a':
        print("You chose to play 'Normal' version")
        new_game(play_game)

    # if user entered 'b',start the quiz but set the marking feature to hard
    elif play_game == 'b':
        print("You chose to play 'Hard' version")
        new_game(play_game)

    # # if user entered 'c', then display the rules of the quiz
    elif play_game == "c":
        display_rules()

# -----Starting a New game for the user-----


def new_game(level_game):

    # set up the variables for the quiz
    guesses = []
    correct_guesses = 0
    question_num = 1

    # the user_name variable is global,so its present through all the functions
    global user_name
    user_name = input("Enter your name: ")

    # nested for loop for iterate through the questions
    for key in questions:
        print("--------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)

        # Convert the user's guess to caps and store it
        guess = input("Enter your guess(A,B,C or D): ").strip()
        guess = guess.upper()

        # call validate_guess method to validate the user guesses
        guess = validate_guess(guess)

        guesses.append(guess)

        # check the answer of the user
        correct_guesses += check_answer(questions.get(key), guess, level_game)
        question_num += 1

    # call display_score method to show the final result to user
    display_score(correct_guesses, guesses)

    # call play_again() to allow user to play the quiz if they wish to
    play_again()


# ----------Validated user guess--------------------------

def validate_guess(option):

    # finding user guess and checking if they had the input: A B C or D
    user_guess = option
    check = True
    while check:
        # if the user had a valid guess, the check feature stops
        if user_guess == "A" or user_guess == "B" or \
                user_guess == "C" or user_guess == "D":
            check = False
        else:
            # if invalid input entered,keep trying until they enter valid input
            print("INVALID INPUT")
            user_guess = input("Please enter a valid option (A,B,C or D): ") \
                .strip()

            user_guess = user_guess.upper()

    return user_guess


# --check_answer method to check whether the user guess is correct or not!--


def check_answer(answer, guess, score_level):
    """
    definition: checks answer,
    returns what to add to a total score...
    """

    # while the user is playing in the easy mode, set this scoring system
    if score_level == "a":
        if answer == guess:
            print("CORRECT")
            return 1
        else:
            print("WRONG")
            return 0

    # while the user is playing in the hard mode, set this scoring system
    elif score_level == 'b':
        if answer == guess:
            print("CORRECT")
            return 1
        else:
            print("WRONG")
            return -1


# -----display_score method to display the score


def display_score(correct_guesses, guesses):
    print()
    print("Getting your Results...")
    print()

    # added sleep to increase the excitement of the final result
    time.sleep(2)

    print("--------------------------")
    print("RESULTS QUIZ 2022")
    print("--------------------------")

    # at the end print all the true answers
    print("ANSWERS: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    # at the end print all the user's guesses
    print("GUESSES: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    actual_score = int(correct_guesses)

    # check whether the score gone to negative value for the Hard level
    if actual_score < 0:
        score = 0
    else:
        score = int(correct_guesses)

    # call display_winning_message method
    display_winning_message(score)


# ----- function to let the user play again -----
def play_again():
    print()
    # printing the menu for option to play again
    menu_functionality()


# ---------------------------------------------


def display_rules():

    # If the user entered c, display the quiz's rules

    print()
    print("===RULES===")
    time.sleep(1)
    print()
    print("In this quiz there will be 11 multi choice\
    questions based on general knowledge")
    time.sleep(2)
    print("You will have to enter A,B,C or D depending\
        what you think is the answer")
    time.sleep(2)
    print("After each question it would be displayed\
        if you got the question right or not")
    time.sleep(2)
    print("At the end of the quiz, your score and answers would be displayed")
    time.sleep(2)
    print()

    menu_functionality()


# display_winning_message method to display the winning message to the Player

def display_winning_message(score):
    if score == 11:
        display_message = "~~EXCELLENT~~"
    elif 8 <= score <= 10:
        display_message = "-Amazing Effort-"
    elif 5 <= score <= 7:
        display_message = "Good Enough!!"
    elif 2 <= score <= 4:
        display_message = "Better Luck Next Time"
    else:
        display_message = "BAD LUCK :("

    print("Hi " + user_name.upper())
    print("Your final score is: " + str(score) + "/11 " + display_message)


# -----call the main method----

# calling the main() function at the end to start the quiz
main()

# Testing the code with Normal mode using HAPPY PATH
"""
***********************************
~~General Knowledge Quiz 2022~~
***********************************


===MENU===
Do you want to play the quiz?
A) Enter 'A' to start the normal quiz
B) Enter 'B' to start the hard quiz
C) Enter 'C' to see the rules of the quiz
D) enter any other key to leave
Enter your choice : A
Enter your name: Riddhimaan
--------------------------
1. What is the largest country by population in the world?:
A. China
B. Russia
C. India
D. United States
Enter your guess(A,B,C or D): a
CORRECT
--------------------------
2. What year did the first world war end?:
A. 1945
B. 1918
C. 1916
D. 1917
Enter your guess(A,B,C or D): b
CORRECT
--------------------------
3. What is the most popular sport in the world?:
A. Cricket
B. Basketball
C. Football
D. Rugby
Enter your guess(A,B,C or D): c
CORRECT
--------------------------
4. What is arachnophobia the fear of?:
A. Insects
B. Frogs
C. Snakes
D. Spiders
Enter your guess(A,B,C or D): d
CORRECT
--------------------------
5. How many dots appear on a dice?:
A. 21
B. 36
C. 32
D. 30
Enter your guess(A,B,C or D): a
CORRECT
--------------------------
6. In what country would you find Mount Kilimanjaro?:
A. Zimbabwe
B. Africa
C. Tanzania
D. Kenya
Enter your guess(A,B,C or D): b
WRONG
--------------------------
7. What is the worlds fastest bird?:
A. Red Hawk
B. Seagull
C. Bald Eagle
D. Peregrine Falcon
Enter your guess(A,B,C or D): c
WRONG
--------------------------
8. Which Football team does Messi play for?:
A. Barcelona
B. PSG
C. Real Madrid
D. Arsenal
Enter your guess(A,B,C or D): d
WRONG
--------------------------
9. How many days in a leap year?:
A. 365
B. 366
C. 364
D. 367
Enter your guess(A,B,C or D): a
WRONG
--------------------------
10. Whats the largest ocean?:
A. Pacific Ocean
B. Atlantic Ocean
C. Indian Ocean
D. East Blue
Enter your guess(A,B,C or D): b
WRONG
--------------------------
11. How many teeth does an adult human have?:
A. 36
B. 34
C. 30
D. 32
Enter your guess(A,B,C or D): c
WRONG

Getting your Results...

--------------------------
RESULTS QUIZ 2022
--------------------------
ANSWERS: A B C D A C D B B A D
GUESSES: A B C D A B C D A B C
Hi RIDDHIMAAN - Your final score is: 5/11 Good Enough!!

Do you want to play the quiz?
A) Enter 'A' to start the normal quiz
B) Enter 'B' to start the hard quiz
C) Enter 'C' to see the rules of the quiz
D) enter any other key to leave
Enter your choice : n
Thanks for trying the quiz!! Goodbye
"""
