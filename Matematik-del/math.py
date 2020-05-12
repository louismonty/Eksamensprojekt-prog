"""
Made by Frederik Ø. Elster
HTX Roskilde
Programmering B 3.4

"""
# Imports
import random
import os
import time


class math_problem:
    def __init__(self,x1, x2, point):
        self.x1 = x1
        self.x2 = x2
        self.point = point
        self.answer = False

        
    def random_numbers(self):
        #2 random numbers 
        self.number_one = random.randrange(self.x1, self.x2 + 1)
        self.number_two = random.randrange(self.x1, self.x2 + 1)
         

    def multiplication(self,count,level):
        # Get random numbers
        self.random_numbers()
        # Make possible to print the math problem
        problem = str(self.number_one) + " * " + str(self.number_two)
        # Calulate the correct answer
        solution = self.number_one * self.number_two
        # Get user input
        user_solution = get_user_solution(problem)
        # Check if user inpu is correct
        answer = check_solution(user_solution, solution, count, self.answer)       
        return answer

    def multiply(self, count, level):
        self.random_numbers()
        problem = str(self.number_one) + " + " + str(self.number_two)
        solution = self.number_one + self.number_two
        user_solution = get_user_solution(problem)
        answer = check_solution(user_solution, solution, count, self.answer)       
        return answer

    def subtracting(self, count, level):
        self.random_numbers()
        problem = str(self.number_one) + " - " + str(self.number_two)
        solution = self.number_one - self.number_two
        user_solution = get_user_solution(problem)
        answer = check_solution(user_solution, solution, count, self.answer)       
        return answer

    def point_score(self, answer,score):
        # Update point score if user input is correct
        if answer == True:
            score += self.point
            return score
        else:
            # if not the score is unchanged 
            return score

# Defines level
level_1 = math_problem(1,3,0.25)
level_2 = math_problem(2,4,0.5)
level_3 = math_problem(3,5,0.75)
level_4 = math_problem(4,6,1)
level_5 = math_problem(5,8,1.25)
level_6 = math_problem(6,9,1.5)
level_7 = math_problem(6,10,1.75)
level_8 = math_problem(7,11,2)
level_9 = math_problem(7,12,2.25)
level_10 = math_problem(8,13,2.5)
level_11 = math_problem(9,14,2.75)
level_12 = math_problem(10,15,3)
level_13 = math_problem(11,16,3.25)
level_14 = math_problem(12,17,3.50)
level_15 = math_problem(13,18,3.75)


# List with all the levels
levels =[level_1,level_2, level_3, level_4, level_5,
        level_6, level_7, level_8, level_9, level_10,
        level_11, level_12, level_13, level_14, level_15]

def get_user_solution(problem):
    # Print math problem
    print(problem, end="")
    # user input as a integer
    result = int(input(" = "))
    return result

def get_user_input(x):
    #Get input to menu
    user_input = int(input("Enter your choice: "))
    #Check if its a possibel answer
    while user_input > x or user_input <= 0:
        print("Invalid menu option.")
        user_input = int(input("Please try again: "))
    else:    
        return user_input


def check_solution(user_solution, solution, count, answer):
    # Check if user input is correct
    if user_solution == solution:
        answer = True
        return answer
    elif user_solution != solution :
        answer = False
        return answer
   
def display_result(total, correct, score):
    #clear terminal
    os.system('cls')

    # The user get 10 math problems.
    if total == 10:
        #Show the score to the user
        print("You answered", total, "questions with", correct, "correct.")
        print("Your score is ", score, " Thank you.")
        time.sleep(5)
        game_loop()



# ==============================================================================
# -- Menu ----------------------------------------------------------------------
# ==============================================================================


def start_menu():
    #clear terminal
    os.system('cls')

    # Check if user wants to start the game
    print("1. Start game")
    print("2. Exit game")
    option = get_user_input(2)

    if option == 1:
        exit = False
    else:
        exit = True
    return exit
    
    
def math_menu():
    #clear terminal
    os.system('cls')

    # User can choose type of math problems
    print("1. Multiply")
    print("2. Subtracting")
    print("3. multiplication")
    option = get_user_input(3)

    if option == 1:
        math_type = "multiply"
    elif option == 2:
        math_type = "subtracting"
    else:
        math_type = "multiplication"
        
    return math_type


def math(total, n, dif):
    # Set correct type of math problem and level
    if dif == "multiply":
        answer = levels[n].multiply(total,n)
    elif dif == "subtracting":
        answer = levels[n].multiply(total,n)
    else: 
        answer = levels[n].multiplication(total,n)
    return answer
    

def difficulty_menu():
    #clear terminal 
    os.system('cls')

    # User can choose difficulty
    print("1. Easy")
    print("2. Normal")
    print("3. Hard")

    level = get_user_input(3)
    #Set n value 
    if level == 1:
        n = 4
    elif level == 2:
        n = 8
    else:
        n = 12
    return n





# ==============================================================================
# -- Game loop -----------------------------------------------------------------
# ==============================================================================

def game_loop():
    # Varibels are 0 
    total = 0
    correct = 0
    streak = 0
    score = 0

    #Check if user wants to exit
    exit = start_menu()
    
    if exit == False:
        # Get necessary information to start the game
        math_type = math_menu()
        n = difficulty_menu()
        start_n = n
        os.system('cls')
    else:
        print("Have a nice day!")
        

    while exit == False:
        #update total value
        # total is equal to the number of math questions
        total += 1

        # Print math problem and compare to user input
        answer = math(total, n, math_type)
         
        if answer == True:
            # Update streak and correct
            streak += 1
            correct += 1
            if streak == 2:
                #update level
                if n == (start_n + 3):
                    # start_n +3 is max level, so level is unchanged
                    n = n
                else:
                    n += 1
                streak = 0
        else:
            
            streak -= 1
            # Check if user need to go down in level
            if streak == -2:
                if n == (start_n - 3):
                    # start_n - 3 is min level, so level is unchanged
                    n = n
                else:
                    n -= 1
                streak = 0
        # Update score
        score = levels[n].point_score(answer, score)
        
        #check if user is done
        display_result(total,correct,score)

        
game_loop()