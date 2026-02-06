from local_functions import *
from random import *
from model_task import *
from numpy import random
from sympy import sqrt, simplify

def generate(task_num: int):
    GEN_DICT = {1: gen_task1, 2: gen_task2, 3: gen_task3, 4: gen_task4,
                5: gen_task5, 6: gen_task6, 7: gen_task7, 8: gen_task8,
                9: gen_task9}
    return GEN_DICT[task_num]()

def gen_task1():

    def swap(number):
        return 1 - number
    
    def side_move(point, direction):
        res = point.copy()
        res[direction] = swap(res[direction])
        return res
    
    SET_OF_VALS = {0, 1}
    SET_OF_POS = {0, 1, 2}
    SET_OF_DIVS = {(1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2)}
    NUM_TO_LETTER = {(0,0,0): 'A', (1,0,0): 'B', (1,1,0): 'C', (0,1,0): 'D',
                     (0,0,1): 'A1', (1,0,1): 'B1', (1,1,1): 'C1', (0,1,1): 'D1'}
    division_of_M = choice(list(SET_OF_DIVS))
    swapped_K = choice(list(SET_OF_POS))
    K_start_pos = [choice(list(SET_OF_VALS)) for _ in range(3)]
    K_end_pos = side_move(K_start_pos, swapped_K)

    K_start_pos_tuple = tuple(K_start_pos)
    K_end_pos_tuple = tuple(K_end_pos)
    K_start = NUM_TO_LETTER.get(K_start_pos_tuple)
    K_end = NUM_TO_LETTER.get(K_end_pos_tuple)

    poss_swaps = SET_OF_POS - {swapped_K}
    swapped_M = choice(list(poss_swaps))
    poss_swaps = poss_swaps - {swapped_M}
    swapped_reserve = choice(list(poss_swaps))

    M_start_pos = [choice(list(SET_OF_VALS)) for _ in range(3)]
    if M_start_pos == K_start_pos or M_start_pos == K_end_pos:
        M_start_pos = side_move(M_start_pos, swapped_reserve)
        M_end_pos = side_move(M_start_pos, swapped_M)
    else:
        M_end_pos = side_move(M_start_pos, swapped_M)
        if M_end_pos == K_start_pos or M_end_pos == K_end_pos:
            M_end_pos = side_move(M_start_pos, swapped_reserve)

    M_start_pos_tuple = tuple(M_start_pos)
    M_end_pos_tuple = tuple(M_end_pos)
    M_start = NUM_TO_LETTER.get(M_start_pos_tuple)
    M_end = NUM_TO_LETTER.get(M_end_pos_tuple)

    return Task.Task1(task_code_number=1, K_start=K_start, K_end=K_end, M_top=division_of_M[0], M_bottom=division_of_M[1], M_start=M_start, M_end=M_end)
    
def gen_task2():
    RANGE = 6
    M1 = 10 # Magic number 1
    ANSWER_LIST = [-2, -1, 1, 2]
    DETER_LIST = [-1,1,2,-2,-4,4,-6,6]

    while True:
        poss_lst_row3 = []
        row1 = [randint(-RANGE, RANGE) for _ in range(3)]
        row2 = [randint(-RANGE, RANGE) for _ in range(3)]

        for x in range(-RANGE, RANGE+1):
            for y in range(-RANGE, RANGE+1):
                for z in range(-RANGE, RANGE+1):
                    a11, a12, a13 = row1
                    a21, a22, a23 = row2
                    a31, a32, a33 = x, y, z
                    
                    current_det = (
                        a11*(a22*a33 - a23*a32) -
                        a12*(a21*a33 - a23*a31) +
                        a13*(a21*a32 - a22*a31)
                    )
                    if current_det in DETER_LIST:
                        poss_lst_row3.append([row1, row2, x, y, z, current_det])
        if len(poss_lst_row3) != 0:
            break
    chosen = choice(poss_lst_row3)

    poss_lst_d = []
    a = [chosen[0][0], chosen[1][0], chosen[2]]
    b = [chosen[0][1], chosen[1][1], chosen[3]]
    c = [chosen[0][2], chosen[1][2], chosen[4]]

    for a0 in ANSWER_LIST:
        for b0 in ANSWER_LIST:
            for c0 in ANSWER_LIST:
                x_d = a0*a[0] + b0*b[0] + c0*c[0]
                y_d = a0*a[1] + b0*b[1] + c0*c[1]
                z_d = a0*a[2] + b0*b[2] + c0*c[2]
                if (abs(x_d) <= M1 and abs(y_d) <= M1 and abs(z_d) <= M1):
                    poss_lst_d.append([x_d, y_d, z_d])

    d = choice(poss_lst_d)

    return Task.Task2(task_code_number=2, a=a, b=b, c=c, d=[d[0], d[1], d[2]])

def gen_task3():
    RANGE = 9
    DISTR = [i for i in range(1, RANGE+1)]
    DISTR_PROB = [(1/i - 0.1) for i in range(1,RANGE+1)]
    DISTR_PROB_NORM = [DISTR_PROB[i]/sum(DISTR_PROB) for i in range(RANGE)]
    ANGLES = {'pi/6': 'sqrt(3)', 'pi/4': 'sqrt(2)', 'pi/3': '2', '2*pi/3': '2', '3*pi/4': 'sqrt(2)', '5*pi/6': 'sqrt(3)'}
    LENGTHS = ['1', '2']

    a_m, a_n, b_m, b_n = random.choice(DISTR, p=DISTR_PROB_NORM, size=4)
    a_m = a_m*(-1)**randint(1,2)
    a_n = a_n*(-1)**randint(1,2)
    b_m = b_m*(-1)**randint(1,2)
    b_n = b_n*(-1)**randint(1,2)
    angle = choice(list(ANGLES.keys()))
    length_m, length_n = choice(LENGTHS), choice(LENGTHS)

    randomising = randint(1,2)
    if randomising == 1:
        length_m = str(simplify(length_m + '*' + ANGLES.get(angle)))
    else:
        length_n = str(simplify(length_n + '*' + ANGLES.get(angle)))

    return Task.Task3(task_code_number=3, a_m=a_m, a_n=a_n, b_m=b_m, b_n=b_n, len_m=length_m, len_n=length_n, angle=angle)

def gen_task4():

    def divisors(num: int):
        divs = {1}
        for i in range(2, round(abs(num)**0.5 + 0.5)):
            if num % i == 0:
                divs.add(num//i)
                divs.add(i)
        return divs

    def LCD(lst: list):
        set_full = divisors(lst[0])
        for i in range(1,len(lst)):
            set_full = set_full.intersection(divisors(lst[i]))
        return max(set_full)
    
    SET_OF_FREES = {'a', 'b', 'c'}
    dict_of_frees = {'a': [], 'b': [], 'c': []}
    x_coord = {'a': 0, 'b': 0, 'c': 0}
    y_coord = {'a': 0, 'b': 0, 'c': 0}
    x_proj = [randint(1,9)*(-1)**randint(1,2) for _ in range(3)]
    y_proj = [randint(1,9)*(-1)**randint(1,2) for _ in range(3)]

    while y_proj == x_proj:
        y_proj = [randint(1,9)*(-1)**randint(1,2) for _ in range(3)]
    randomised_free = x_proj
    while randomised_free == x_proj or randomised_free == y_proj:
        randomised_free = [randint(1,20)*(-1)**randint(1,2) for _ in range(3)]

    randomised_free_letter = choice(list(SET_OF_FREES))
    leftover_set = SET_OF_FREES - set(randomised_free_letter)
    randomised_proj_free_letter = choice(list(leftover_set))
    final_letter = choice(list(leftover_set - set(randomised_proj_free_letter)))
    chosen_proj = choice([x_proj, y_proj])
    randomised_proj_free = chosen_proj.copy()

    if randomised_proj_free == x_proj:
        x_coord[randomised_proj_free_letter] = 1
        y_coord[randomised_free_letter] = 1
        y_coord[final_letter] = LCD([y_proj[i] - randomised_free[i] for i in range(3)])*(-1)**randint(1,2)
        final = [(y_proj[i] - randomised_free[i]) // y_coord[final_letter] for i in range(3)]
    else:
        y_coord[randomised_proj_free_letter] = 1
        x_coord[randomised_free_letter] = 1
        x_coord[final_letter] = LCD([x_proj[i] - randomised_free[i] for i in range(3)])*(-1)**randint(1,2)
        final = [(x_proj[i] - randomised_free[i]) // x_coord[final_letter] for i in range(3)]

    dict_of_frees[randomised_free_letter] = randomised_free
    dict_of_frees[randomised_proj_free_letter] = randomised_proj_free
    dict_of_frees[final_letter] = final

    return Task.Task4(task_code_number=4,
                      x_a = x_coord['a'], x_b = x_coord['b'], x_c = x_coord['c'],
                      y_a = y_coord['a'], y_b = y_coord['b'], y_c = y_coord['c'],
                      a = dict_of_frees['a'], b = dict_of_frees['b'], c = dict_of_frees['c'])

def gen_task5():
    RANGE = 9
    M1 = 15 # Magic number 1
    poss_lst_yz = []

    for AB_y in range(-RANGE, RANGE + 1):
            for AB_z in range(-RANGE, RANGE + 1):
                for AC_y in range(-RANGE, RANGE + 1):
                    for AC_z in range(-RANGE, RANGE + 1):
                        if 0 < abs(AB_y*AC_z - AB_z*AC_y) < RANGE + 1:
                            poss_lst_yz.append([AB_y, AC_y, AB_z, AC_z])

    chosen_yz = choice(poss_lst_yz)
    AB_y, AC_y, AB_z, AC_z = chosen_yz
    poss_lst_x = []

    for AB_x in range(-RANGE, RANGE + 1):
        for AC_x in range(-RANGE, RANGE + 1):
            if (0 < abs(AB_x*AC_y - AB_y*AC_x) < 10) and (0 < abs(-AB_x*AC_z + AB_z*AC_x) < RANGE + 1):
                poss_lst_x.append([AB_x, AC_x])

    chosen_x = choice(poss_lst_x)
    AB_x, AC_x = chosen_x
    AB, AC = [AB_x, AB_y, AB_z], [AC_x, AC_y, AC_z]
    A = [randint(-(RANGE + 1), RANGE + 1) for _ in range(3)]
    B = [A[i] + AB[i] for i in range(3)]
    C = [A[i] + AC[i] for i in range(3)]

    for i in range(3):
        if B[i] > M1 or C[i] > M1:
            A[i], B[i], C[i] = A[i] - max([B[i], C[i]]) + M1, B[i] - max([B[i], C[i]]) + M1, C[i] - max([B[i], C[i]]) + M1
        if B[i] < -M1 or C[i] < -M1:
            A[i], B[i], C[i] = A[i] - min([B[i], C[i]]) - M1, B[i] - min([B[i], C[i]]) - M1, C[i] - min([B[i], C[i]]) - M1

    return Task.Task5(task_code_number=5, A=A, B=B, C=C)

def gen_task6():
    ANGLES = ['pi/6', 'pi/4', 'pi/3', '2*pi/3', '3*pi/4', '5*pi/6']
    M1 = 4
    M2 = 5
    a_m, a_n, b_m, b_n = [randint(1,M1)*(-1)**randint(1,2) for _ in range(4)]
    while (a_m*b_n - a_n*b_m == 0):
        a_m, a_n, b_m, b_n = [randint(1,M1)*(-1)**randint(1,2) for _ in range(4)]
    length_m, length_n = [randint(1,M2) for _ in range(2)]
    angle = choice(ANGLES)
    subtask = randint(1,2)

    return Task.Task6(task_code_number=6, subtask=subtask,
                      a_m=a_m, a_n=a_n, b_m=b_m, b_n=b_n, 
                      len_m=length_m, len_n=length_n, angle=angle)

def gen_task7():

    def gen_subtask1(row1, row2, row3, subtask):
        return Task.Task7(task_code_number=7, subtask=subtask, 
                          A=[], B=[], C=[], D=[], a=[row1[0], row2[0], row3[0]], 
                          b=[row1[1], row2[1], row3[1]], c=[row1[2], row2[2], row3[2]])
    
    def gen_subtask2(row1, row2, row3, subtask):
        M1 = 15
        a=[row1[0], row2[0], row3[0]]
        b=[row1[1], row2[1], row3[1]]
        c=[row1[2], row2[2], row3[2]]
        A = [randint(-(RANGE + 1), RANGE + 1) for _ in range(3)]
        B = [A[i] + a[i] for i in range(3)]
        C = [A[i] + b[i] for i in range(3)]
        D = [A[i] + c[i] for i in range(3)]

        for i in range(3):
            if B[i] > M1 or C[i] > M1 or D[i] > M1:
                A[i], B[i] = A[i] - max([B[i], C[i], D[i]]) + M1, B[i] - max([B[i], C[i], D[i]]) + M1
                C[i], D[i] = C[i] - max([B[i], C[i], D[i]]) + M1, D[i] - max((B[i], C[i], D[i])) + M1
            if B[i] < -M1 or C[i] < -M1 or D[i] < -M1:
                A[i], B[i] = A[i] - min([B[i], C[i], D[i]]) - M1, B[i] - min([B[i], C[i], D[i]]) - M1
                C[i], D[i] = C[i] - min([B[i], C[i], D[i]]) - M1, D[i] - min([B[i], C[i], D[i]]) - M1

        return Task.Task7(task_code_number=7, subtask=subtask, 
                          A=A, B=B, C=C, D=D, a=[], b=[], c=[])
    
    RANGE = 9
    randomiser_ans = randint(0,1)
    while True:
        poss_lst_row3 = []
        row1 = [randint(-RANGE, RANGE) for _ in range(3)]
        row2 = [randint(-RANGE, RANGE) for _ in range(3)]

        for x in range(-RANGE, RANGE+1):
            for y in range(-RANGE, RANGE+1):
                for z in range(-RANGE, RANGE+1):
                    a11, a12, a13 = row1
                    a21, a22, a23 = row2
                    a31, a32, a33 = x, y, z
                    
                    current_det = (
                        a11*(a22*a33 - a23*a32) -
                        a12*(a21*a33 - a23*a31) +
                        a13*(a21*a32 - a22*a31)
                    )
                    if abs(current_det) <= RANGE*randomiser_ans:
                        poss_lst_row3.append([row1, row2, x, y, z, current_det])
        if len(poss_lst_row3) != 0:
            break
    chosen = choice(poss_lst_row3)
    row3 = [chosen[i] for i in range(2,5)]
    randomiser_task = randint(1,3)
    DICT_TASK = {1: gen_subtask1, 2: gen_subtask2, 3: gen_subtask2}
    return DICT_TASK[randomiser_task](row1, row2, row3, randomiser_task)

def gen_task8():
    subtask = randint(1,2)
    RANGE = 9
    while True:
        poss_lst_row3 = []
        row1 = [randint(-RANGE, RANGE) for _ in range(3)]
        row2 = [randint(-RANGE, RANGE) for _ in range(3)]

        for x in range(-RANGE, RANGE+1):
            for y in range(-RANGE, RANGE+1):
                for z in range(-RANGE, RANGE+1):
                    a11, a12, a13 = row1
                    a21, a22, a23 = row2
                    a31, a32, a33 = x, y, z
                    
                    current_det = (
                        a11*(a22*a33 - a23*a32) -
                        a12*(a21*a33 - a23*a31) +
                        a13*(a21*a32 - a22*a31)
                    )
                    if 0 < abs(current_det) <= RANGE:
                        poss_lst_row3.append([row1, row2, x, y, z, current_det])
        if len(poss_lst_row3) != 0:
            break
    chosen = choice(poss_lst_row3)
    row3 = [chosen[i] for i in range(2,5)]
    M1 = 15
    a=[row1[0], row2[0], row3[0]]
    b=[row1[1], row2[1], row3[1]]
    c=[row1[2], row2[2], row3[2]]
    A = [randint(-(RANGE + 1), RANGE + 1) for _ in range(3)]
    B = [A[i] + a[i] for i in range(3)]
    C = [A[i] + b[i] for i in range(3)]
    D = [A[i] + c[i] for i in range(3)]

    for i in range(3):
        if B[i] > M1 or C[i] > M1 or D[i] > M1:
            A[i], B[i] = A[i] - max([B[i], C[i], D[i]]) + M1, B[i] - max([B[i], C[i], D[i]]) + M1
            C[i], D[i] = C[i] - max([B[i], C[i], D[i]]) + M1, D[i] - max((B[i], C[i], D[i])) + M1
        if B[i] < -M1 or C[i] < -M1 or D[i] < -M1:
            A[i], B[i] = A[i] - min([B[i], C[i], D[i]]) - M1, B[i] - min([B[i], C[i], D[i]]) - M1
            C[i], D[i] = C[i] - min([B[i], C[i], D[i]]) - M1, D[i] - min([B[i], C[i], D[i]]) - M1
    return Task.Task8(task_code_number=8, subtask=subtask, A=A, B=B, C=C, H=D)

def gen_task9():
    RANGE = 5
    A1, B1, C1 = [randint(-RANGE, RANGE) for _ in range(3)]
    A2, B2, C2 = [randint(-RANGE, RANGE) for _ in range(3)]
    D1, D2 = [randint(-3*RANGE, 3*RANGE) for _ in range(2)]
    while (A1 == 0) and (B1 == 0) and (C1 == 0):
        A1, B1, C1 = [randint(-RANGE, RANGE) for _ in range(3)]
    while (A2 == 0) and (B2 == 0) and (C2 == 0):
        A2, B2, C2 = [randint(-RANGE, RANGE) for _ in range(3)]
    while (A1*B2 - B1*A2) == 0 or (C2*A1 - A2*C1) == 0 or (B1*C2 - C1*B2) == 0:
        A2, B2, C2 = [randint(-RANGE, RANGE) for _ in range(3)]
    return Task.Task9(task_code_number=9, A1=A1, B1=B1, C1=C1, D1=D1, A2=A2, B2=B2, C2=C2, D2=D2)
