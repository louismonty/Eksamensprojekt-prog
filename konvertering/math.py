"""
Made by Frederik Ø. Elster
HTX Roskilde
Programmering B 3.4

reee
"""
import random
import os


class math_problem:
    def __init__(self,x1, x2, point):
        self.x1 = x1
        self.x2 = x2
        self.point = point
        self.answer = False
        self.list = []
        
    def random_numbers(self):
        self.number_one = random.randrange(self.x1, self.x2)
        self.number_two = random.randrange(self.x1, self.x2)
        self.list.append([self.number_one, self.number_two])
        print(self.list)

    def multiplication(self,count,level):
        self.random_numbers()
        problem = str(self.number_one) + " * " + str(self.number_two)
        solution = self.number_one * self.number_two
        user_solution = get_user_solution(problem)
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
        if answer == True:
            score += self.point
            return score
        else:
            return score

# Defines level
level_1 = math_problem(1,3,0.25)
level_2 = math_problem(2,4,0.5)
level_3 = math_problem(3,5,0.75)
level_4 = math_problem(4,6,1)
level_5 = math_problem(5,8,1.25)
level_6 = math_problem(6,9,1.5)
level_7 = math_problem(7,10,1.75)
level_8 = math_problem(8,11,2)
level_9 = math_problem(9,12,2.25)
level_10 = math_problem(10,13,2.5)
level_11 = math_problem(11,14,2.75)
level_12 = math_problem(12,15,3)
level_13 = math_problem(13,16,3.25)
level_14 = math_problem(14,17,3.50)
level_15 = math_problem(15,18,3.75)



levels =[level_1,level_2, level_3, level_4, level_5,
        level_6, level_7, level_8, level_9, level_10,
        level_11, level_12, level_13, level_14, level_15]

def get_user_solution(problem):
    print(problem, end="")
    result = int(input(" = "))
    return result

def check_solution(user_solution, solution, count, answer):
    if user_solution == solution:
        answer = True
        return answer
    elif user_solution != solution :
        answer = False
        return answer
   
def display_result(total, correct, score):
    if total == 10:
        print("You answered", total, "questions with", correct, "correct.")
        print("Your score is ", score, " Thank you.")
        game_loop()



# ==============================================================================
# -- Menu ----------------------------------------------------------------------
# ==============================================================================


def start_menu():
    os.system('cls')
    print("1. Start game")
    print("2. Exit game")
    option = get_user_input(2)

    if option == 1:
        exit = False
    else:
        exit = True
    return exit
    
    
def math_menu():
    os.system('cls')
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
    if dif == "multiply":
        answer = levels[n].multiply(total,n)
    elif dif == "subtracting":
        answer = levels[n].multiply(total,n)
    else: 
        answer = levels[n].multiplication(total,n)
    return answer
    

def difficulty_menu():
    os.system('cls')
    print("1. Easy")
    print("2. Normal")
    print("3. Hard")

    level = get_user_input(3)
    if level == 3:
        n = 0
    elif level == 7:
        n = 1
    else:
        n = 11
    return n


def get_user_input(x):
    user_input = int(input("Enter your choice: "))
    while user_input > x or user_input <= 0:
        print("Invalid menu option.")
        user_input = int(input("Please try again: "))
    else:
        return user_input


# ==============================================================================
# -- Game loop -----------------------------------------------------------------
# ==============================================================================

def game_loop():
    
    total = 0
    correct = 0
    streak = 0
    score = 0

    exit = start_menu()
    
    if exit == False:
        math_type = math_menu()
        n = difficulty_menu()
        start_n = n
        os.system('cls')
    else:
        print("Have a nice day!")
        
    while exit == False:
        total += 1
        
        answer = math(total, n, math_type)
         
        if answer == True:
            streak += 1
            correct += 1
            if streak == 2:
                if n == (start_n + 3):
                    n = n
                else:
                    n += 1
                streak = 0
        else:
            if streak == 0 or streak == -1:
                streak -= 1
                if streak == -2:
                    if n ==  (start_n - 3):
                        n = n
                    else:
                        n -= 1
            streak = 0

        score = levels[n].point_score(answer, score)
        display_result(total,correct,score)

        """
        #Test variabels
        print("score:", score)
        print("streak:", streak)
        print("n:", n)
        print("correct:", correct)
        print("Total:", total)
        """
     
game_loop()