import datetime
from re import A
# Asking for users name so they can be referenced
Name = input ( "What is your name? ")
time = datetime.datetime.now()

# All the questions and possible answers for the game
Q1 = "Question 1: What season did the Arsenal team known as the invincibles play ? A. 2000-01 B. 2003-04 C. 2005-06 D. 2002-03 "
Q2 = "Question 2: What number did Micheal Jordan wear when we played for the Wizards A. 23 B. 25 C. 45 D. 24 "
Q3 = "Question 3: What colour is the most popular toilet paper in France? A.Blue, B. White, C. Pink, D. Green "
Q4 = "Question 4: What is the strongest muscle in the body ? A Hamstring, B. Abdominals C. Quadriceps, D. Tougne "
Q5 = "Question 5: What is the smallest country in the world ? A. Australia, B. New Zealand, C. Vatican City, D. Monaco "
Q6 = "Question 6: Is it true of false that an Armadilos shell bullet proof A. False, B. True "
Q7 = "Question 7: What does a cow drink ? A. Water, B. Moutain dew, C. Milk, D. Solo "
Q8 = "Question 8: How deep is the Mariana Trench ? A. 36,201 meters, B. 38,204 feet, C. 36,201 feet, D. 11,454 meters "
Q9 = "Question 9: How tall is Shaquille O'neal ? A. 7'4, B. 7'1, C. 7'2, D. 7' "
Q10 = "Question 10: What is the best coding boot camp run by ? A. Coder Academy, B. Harvard University, C. Google, D. Youtube "

# Answers to all of the questions 
count = 0
Questions = [(Q1, "B"), (Q2, "A"), (Q3, "C"), (Q4, "D"), (Q5, "C"), (Q6, "B"), (Q7, "A"), (Q8, "C"), (Q9, "B"), (Q10, "A")]

# Explaining what to do with a correct answer or a wrong answer
def question(question, correct):
    selection = input(question).upper()
    print(selection)
    if selection == correct:
        print(f"Good job {Name}")
        return True
    else:
        print("Incorrect")
        return False

# How the game will responded to whether the user wants to play or get help
def game():
    answer = input ("would you like to play the game yes/no ? type 'help' for more information ")
    count = 0
    while answer == "yes" or answer == "help":
        if answer == "help":
            import help
        print ("It is time to play")
        for number, correct_answer in Questions:
            if question(number, correct_answer):
                count += 1
        print(f"{Name} you got", count, "questions correct" )
        answer = input ("Do you want to play again? yes / no ")
    if answer == "no":
        print (f"Ok {Name}, enjoy the rest of your day " + time.strftime(" %d-%m-%Y "))
        return
        
game()

# Have run tests with correct answers with and with out correct answers, the code will always display the right amount of correct answer and give the ability to try again. This works and will rather re run the gme or terminate the code 
# Have also run tests where i have asked for help at the start of the game and all features work correctly after that as well 