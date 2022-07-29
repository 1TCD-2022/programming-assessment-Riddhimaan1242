"""
Filename: quiz2022.py
Author: Riddhimaan
Date: 8/07/2022
Description: This program is a general knowledge quiz, that will test the user's knowledge through various questions

"""
# dictionary used for predefined value of quiz questions
quiz_questions = {
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

# 2D list used for predefined value of quiz answers
quiz_options = [
                ["A. China", "B. Russia", "C. India", "D. United States"],
                ["A. 1945", "B. 1918", "C. 1916", "D. 1917"],
                ["A. Cricket", "B. Basketball", "C. Football", "D. Rugby"],
                ["A. Insects", "B. Frogs", "C. Snakes", "D. Spiders"],
                ["A. 21", "B. 36", "C. 32", "D. 30"],
                ["A. Zimbabwe", "B. Africa", "C. Tanzania", "D. Kenya"],
                ["A. Red Hawk", "B. Seagull", "C. Bald Eagle", "D. Peregrine Falcon"],
                ["A. Barcelona", "B. PSG", "C. Real Madrid", "D. Arsenal"],
                ["A. 365", "B. 366", "C. 364", "D. 367"],
                ["A. Pacific Ocean", "B. Atlantic Ocean", "C. Indian Ocean", "D. East Blue"],
                ["A. 36", "B. 34", "C. 30", "D. 32"]
            ]

# Start of program menu to allow user to start or stop the quiz
print("********************************************************************")
print("******************* GENERAL KNOWLEDGE QUIZ 2022 **********************")
print("********************************************************************")
print()

# input function for user to decide if the user wants to play or not
print("Do you want to play the quiz? Enter 'yes' to play, or enter any other key to leave-")
starting_game = input("User choice: ")

# convert user input into Upper case Like: (YeS/YES/yEs --> yes)  -> YES
starting_game = starting_game.lower()

# if user entered yes, the quiz starts
if starting_game == 'yes':
    # -------------------------------------------------------
    def start_quiz():
        # guesses array to store user options
        guesses = []
        correct_guesses = 0
        question_num = 1

        # Used nested for loop to loop through questions and the options.
        # First loop to loop through the questions and inner loop to loop through the options.
        for key in quiz_questions:
            print("--------------------------")
            print(key)
            for i in quiz_options[question_num - 1]:
                print(i)
            guess = input("Enter (A,B,C or D): ")
            # convert the option that entered by the user in upper case
            guess = guess.upper()
            # add the user guess in the guesses list
            guesses.append(guess)

            # correct_guesses
            if quiz_questions.get(key) == guess:
                print("C O R R E C T!")
                correct_guesses += 1
            else:
                print("W R O N G")
            # increase the value of question_num by one
            question_num += 1

        # display the final result
        print("--------------------------")
        print("QUIZ 2022 RESULTS")
        print("--------------------------")

        # calculate the score and convert it into integer
        score = int((correct_guesses / len(quiz_questions)) * 100)
        # convert the final score into string
        print("Your final score is: " + str(score) + "%")

    # call start_quiz method to start the game
    start_quiz()

print("Thanks for trying this out, Goodbye!")
