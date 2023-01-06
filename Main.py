# -------------------------
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


# -------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
          print(questions.get(i), end="")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end="")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")


# -------------------------
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------


questions = {
    "How much seconds in an hour?: ": "D",
    "How much was the most expensive book ever purchased?: ": "B",
    "For what activity did the Olympics give out medals for in the past?: ": "C",
    "How much Earths can fit inside the Sun?: ": "A"
}

options = [["A. 36,000 seconds", "B. 4,600 seconds", "C. 3,000 seconds", "D. 3,600 seconds"],
           ["A. 15 million", "B. 30.8 million", "C. 4.5 million", "D. 2.7 million"],
           ["A. Debate", "B. Writing", "C. Art", "D. Comedy"],
           ["A. 1 to 1.3 million", "B. 2.5 million", "C. 4 million", "D. 500 thousand to 900 thousand"]]

new_game()

while play_again():
    new_game()

print("Thank you for playing!")