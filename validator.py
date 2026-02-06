from local_functions import *
from model_task import *
from model_solution import *
from solver import *
from sympy import sqrt, symbols, Eq, solve, simplify, asin, pi, cos, sin, N

def valid(user_input: Answer):
    DICT_OF_TASKS = {1: valid_task1, 2: valid_task2, 3: valid_task3, 4: valid_task4,
                     5: valid_task5, 6: valid_task6, 7: valid_task7, 8: valid_task8,
                     9: valid_task9, 10: valid_task10}
    print(user_input)
    return DICT_OF_TASKS[user_input.task.task_code_number](user_input)

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
        true_solution = solve_task4(user_input.task)
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
        check_a_pos = abs(N(true_solution.n0_x) - N(user_solution.n0_x)) < EPS
        check_b_pos = abs(N(true_solution.n0_y) - N(user_solution.n0_y)) < EPS
        check_c_pos = abs(N(true_solution.n0_z) - N(user_solution.n0_z)) < EPS
        check_a_neg = abs(N(true_solution.n0_x) + N(user_solution.n0_x)) < EPS
        check_b_neg = abs(N(true_solution.n0_y) + N(user_solution.n0_y)) < EPS
        check_c_neg = abs(N(true_solution.n0_z) + N(user_solution.n0_z)) < EPS
        return (check_a_pos and check_b_pos and check_c_pos) or (check_a_neg and check_b_neg and check_c_neg)
    except:
        return False
    
def valid_task6(user_input: Answer):
    try:
        EPS = 0.001
        true_solution = solve_task6(user_input.task)
        user_solution = user_input.answer
        check_answer = abs(N(true_solution.answer) - N(user_solution.answer)) < EPS
        return check_answer
    except:
        return False

def valid_task7(user_input: Answer):
    try:
        true_solution = solve_task7(user_input.task)
        user_solution = user_input.answer
        check_a = true_solution.answer == user_solution.answer
        check_b = abs(true_solution.det) == abs(user_solution.det)
        return check_a and check_b
    except:
        return False

def valid_task8(user_input: Answer):
    try:
        EPS = 0.001
        true_solution = solve_task8(user_input.task)
        user_solution = user_input.answer
        check_a = abs(N(true_solution.Volume) - N(user_solution.Volume)) < EPS
        check_b = abs(N(true_solution.Surf_area) - N(user_solution.Surf_area)) < EPS
        check_c = abs(N(true_solution.height) - N(user_solution.height)) < EPS
        return check_a and check_b and check_c
    except:
        return False
    
def valid_task9(user_input: Answer):
    try:
        EPS = 0.001
        true_solution = solve_task9(user_input.task)
        user_solution = user_input.answer
        check_answer = abs(N(true_solution.answer) - N(user_solution.answer)) < EPS
        return check_answer
    except:
        return False

def valid_task10(user_input: Answer):
    try:
        EPS = 0.001
        true_solution = solve_task10(user_input.task)
        user_solution = user_input.answer
        true_n = [true_solution.surf_a, true_solution.surf_b, true_solution.surf_c]
        user_n = [user_solution.surf_a, user_solution.surf_b, user_solution.surf_c]
        cross_surface = [true_n[1]*user_n[2] - user_n[1]*true_n[2], 
                         user_n[0]*true_n[2] - true_n[0]*user_n[2], 
                         true_n[0]*user_n[1] - user_n[0]*true_n[1]]
        check_surface = (cross_surface.count(0) == 3)
        check_distance = abs(N(true_solution.distance) - N(user_solution.distance)) < EPS
        return check_surface and check_distance
    except:
        return False

user_inp = Answer(answer=Solution.Solution_Task5(n0_x='0.817', n0_y='-sqrt(6)/6', n0_z='sqrt(6)/6'), 
                  task=Task.Task5(task_code_number=5, A=[10,-9,-6], B=[12,-14,-15], C=[10,-7,-4]))

DICT_OF_TASKS = {1: valid_task1, 2: valid_task2, 3: valid_task3, 4: valid_task4,
                 5: valid_task5, 6: valid_task6, 7: valid_task7, 8: valid_task8}

#print(DICT_OF_TASKS.get(user_inp.task_num))