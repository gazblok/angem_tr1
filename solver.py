from local_functions import *
from model_task import *
from model_solution import *
from fractions import Fraction
from sympy import sqrt, symbols, Eq, solve, simplify, asin, cos, sin
import numpy as np

def solvers(task: Task):
    SOLVERS_DICT = {1: solve_task1, 2: solve_task2, 3: solve_task3, 4: solve_task4, 
                    5: solve_task5, 6: solve_task6, 7: solve_task7, 8: solve_task8,
                    9: solve_task9}
    return SOLVERS_DICT[task.task_code_number](task)

def solve_task1(task: Task.Task1):
    LETTER_TO_NUM = {'A': [0,0,0], 'B': [1,0,0], 'C': [1,1,0], 'D': [0,1,0],
                    'A1': [0,0,1], 'B1': [1,0,1], 'C1': [1,1,1], 'D1': [0,1,1]}
    K1 = LETTER_TO_NUM.get(task.K_start)
    K2 = LETTER_TO_NUM.get(task.K_end)
    p = task.M_top
    q = task.M_bottom
    M1 = LETTER_TO_NUM.get(task.M_start)
    M2 = LETTER_TO_NUM.get(task.M_end)
    K = [(K1[i] + K2[i]) / 2 for i in range(3)]
    M = [(p*M2[i] + q*M1[i]) / (p + q) for i in range(3)]
    KM = [str(Fraction(M[i] - K[i]).limit_denominator()) for i in range(3)]
    return Solution.Solution_Task1(KM_a=KM[0], KM_b=KM[1], KM_c=KM[2])

def solve_task2(task: Task.Task2):
    a = task.a
    b = task.b
    c = task.c
    d = task.d
    D = np.dot(a, np.cross(b, c))
    Dx = np.dot(d, np.cross(b, c))
    Dy = np.dot(a, np.cross(d, c))
    Dz = np.dot(a, np.cross(b, d))
    return Solution.Solution_Task2(d_a=Dx//D, d_b=Dy//D, d_c=Dz//D)

def solve_task3(task: Task.Task3):
    a_m = task.a_m
    a_n = task.a_n
    b_m = task.b_m
    b_n = task.b_n
    angle = simplify(task.angle)
    len_m = simplify(task.len_m)
    len_n = simplify(task.len_n)

    mn_dot = len_m*len_n*cos(angle)
    ab_dot = a_m*b_m*len_m**2 + (a_m*b_n + a_n*b_m)*mn_dot + a_n*b_n*len_n**2
    a_dot = a_m*a_m*len_m**2 + (a_m*a_n + a_n*a_m)*mn_dot + a_n*a_n*len_n**2
    b_dot = b_m*b_m*len_m**2 + (b_m*b_n + b_n*b_m)*mn_dot + b_n*b_n*len_n**2
    ans = ab_dot / (sqrt(a_dot) * sqrt(b_dot))

    return Solution.Solution_Task3(answer=str(ans))

def solve_task4(task: Task.Task4):
    x = [task.x_a*task.a[i] + task.x_b*task.b[i] + task.x_c*task.c[i] for i in range(3)]
    y = [task.y_a*task.a[i] + task.y_b*task.b[i] + task.y_c*task.c[i] for i in range(3)]
    ans = simplify(np.dot(x, y) / sqrt(y[0]**2 + y[1]**2 + y[2]**2))
    return Solution.Solution_Task4(answer=str(ans))

def solve_task5(task: Task.Task5):
    A = task.A
    B = task.B
    C = task.C
    AB = [B[i] - A[i] for i in range(3)]
    AC = [C[i] - A[i] for i in range(3)]
    n = np.cross(AB, AC)
    length_n = sqrt(n[0]**2 + n[1]**2 + n[2]**2)
    n0 = [str(n[i] / length_n) for i in range(3)]
    return Solution.Solution_Task5(n0_x=n0[0], n0_y=n0[1], n0_z=n0[2])

def solve_task6(task: Task.Task6):
    AREA_MOD = task.subtask
    a_m, a_n, b_m, b_n = task.a_m, task.a_n, task.b_m, task.b_n
    m, n, angle = task.len_m, task.len_n, task.angle
    mn_cross = m*n*sin(angle)
    ab_cross = abs(a_m*b_n - a_n*b_m)*mn_cross
    return Solution.Solution_Task6(answer=str(ab_cross / AREA_MOD))

def solve_task7(task: Task.Task7):
    subtask = task.subtask
    a = task.a
    b = task.b
    c = task.c
    if subtask > 1:
        a = [task.B[i] - task.A[i] for i in range(3)]
        b = [task.C[i] - task.A[i] for i in range(3)]
        c = [task.D[i] - task.A[i] for i in range(3)]
    det = np.dot(a, np.cross(b, c))
    return Solution.Solution_Task7(det=det, answer=(not det))

def solve_task8(task: Task.Task8):
    COEFFS_DICT = {1: [1/6, 1/2, 3], 2: [1, 1, 1]}
    a = [task.B[i] - task.A[i] for i in range(3)]
    b = [task.C[i] - task.A[i] for i in range(3)]
    c = [task.H[i] - task.A[i] for i in range(3)]
    subtask = task.subtask
    vol_coef, surf_coef, height_coef = COEFFS_DICT[subtask]
    Volume = abs(np.dot(a, np.cross(b, c))*vol_coef)
    Surf_area_vect = np.cross(b, c)
    Surf_area = sqrt(sum([Surf_area_vect[i]**2 for i in range(3)]))*surf_coef
    height = (Volume/Surf_area)*height_coef
    return Solution.Solution_Task8(Volume=str(Volume), Surf_area=str(Surf_area), height=str(height))

def solve_task9(task: Task.Task9):
    norm_1 = [task.A1, task.B1, task.C1]
    norm_2 = [task.A2, task.B2, task.C2]
    norm_1_len = sqrt(norm_1[0]**2 + norm_1[1]**2 + norm_1[2]**2)
    norm_2_len = sqrt(norm_2[0]**2 + norm_2[1]**2 + norm_2[2]**2)
    answer = abs(np.dot(norm_1, norm_2) / (norm_1_len*norm_2_len))
    return Solution.Solution_Task9(answer=str(answer))
