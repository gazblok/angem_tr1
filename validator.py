from local_functions import *
from model_task import *
from model_solution import *
from solver import *
from sympy import sqrt, symbols, Eq, solve, simplify, asin, pi, cos, sin, N

def valid_task1(user_input: Answer):
    try:
        EPS = 0.001
        true_solution = solve_task1(user_input.task)
        user_solution = user_input.answer
        check_a = abs(N(true_solution.KM_a) - N(user_solution.KM_a)) < EPS
        check_b = abs(N(true_solution.KM_b) - N(user_solution.KM_b)) < EPS
        check_c = abs(N(true_solution.KM_c) - N(user_solution.KM_c)) < EPS
        return check_a and check_b and check_c
    except:
        return False

def valid_task2(user_input: Answer):
    try:
        true_solution = solve_task2(user_input.task)
        user_solution = user_input.answer
        check_a = true_solution.d_a == user_solution.d_a
        check_b = true_solution.d_b == user_solution.d_b
        check_c = true_solution.d_c == user_solution.d_c
        return check_a and check_b and check_c
    except:
        return False
    
def valid_task3(user_input: Answer):
    try:
        EPS = 0.001
        true_solution = solve_task3(user_input.task)
        user_solution = user_input.answer
        check_answer = abs(N(true_solution.answer) - N(user_solution.answer)) < EPS
        return check_answer
    except:
        return False
    
def valid_task4(user_input: Answer):
    try:
        EPS = 0.001
        true_solution = solve_task3(user_input.task)
        user_solution = user_input.answer
        check_answer = abs(N(true_solution.answer) - N(user_solution.answer)) < EPS
        return check_answer
    except:
        return False
    
def valid_task5(user_input: Answer):
    try:
        EPS = 0.001
        true_solution = solve_task5(user_input.task)
        user_solution = user_input.answer
        check_a = abs(N(true_solution.n0_x) - N(user_solution.n0_x)) < EPS
        check_b = abs(N(true_solution.n0_y) - N(user_solution.n0_y)) < EPS
        check_c = abs(N(true_solution.n0_z) - N(user_solution.n0_z)) < EPS
        return check_a and check_b and check_c
    except:
        return False

user_inp = Answer(task_num=5, answer=Solution.Solution_Task5(n0_x='0.818', n0_y='-sqrt(6)/6', n0_z='sqrt(6)/6'), 
                  task=Task.Task5(A=[10,-9,-6], B=[12,-14,-15], C=[10,-7,-4]))

DICT_OF_TASKS = {1: valid_task1(user_inp), 2: valid_task2(user_inp), 3: valid_task3(user_inp),
                 4: valid_task4(user_inp), 5: valid_task5(user_inp)}
#print(DICT_OF_TASKS.get(user_inp.task_num))