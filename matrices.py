import random

while True:
    poss_lst = []
    row1 = [random.randint(-6, 6) for _ in range(3)]
    row2 = [random.randint(-6, 6) for _ in range(3)]
    deter = [-1,1,2,-2,-4,4,-6,6]
    # Перебираем третью строку
    for x in range(-6, 7):
        for y in range(-6, 7):
            for z in range(-6, 7):
                # Вычисляем определитель
                a11, a12, a13 = row1
                a21, a22, a23 = row2
                a31, a32, a33 = x, y, z
                
                current_det = (
                    a11*(a22*a33 - a23*a32) -
                    a12*(a21*a33 - a23*a31) +
                    a13*(a21*a32 - a22*a31)
                )
                if current_det in deter:
                    poss_lst.append([row1, row2, x, y, z, current_det])
    if len(poss_lst) != 0:
        break
chosen = random.choice(poss_lst)

poss_lst_2 = []
a = [chosen[0][0], chosen[1][0], chosen[2]]
b = [chosen[0][1], chosen[1][1], chosen[3]]
c = [chosen[0][2], chosen[1][2], chosen[4]]
for a0 in [-2, -1, 1, 2]:
    for b0 in [-2, -1, 1, 2]:
        for c0 in [-2, -1, 1, 2]:
            x_d = a0*a[0] + b0*b[0] + c0*c[0]
            y_d = a0*a[1] + b0*b[1] + c0*c[1]
            z_d = a0*a[2] + b0*b[2] + c0*c[2]
            if (abs(x_d) <= 10 and abs(y_d) <= 10 and abs(z_d) <= 10):
                poss_lst_2.append([x_d, y_d, z_d])
chosen_2 = random.choice(poss_lst_2)