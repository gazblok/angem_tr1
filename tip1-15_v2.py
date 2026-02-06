from sympy import sqrt, symbols, Eq, solve, simplify, asin, pi, cos, sin, evaluate
from local_functions import flat, dots, line
import numpy as np
from fractions import Fraction

MAIN = 17
while MAIN != 0:
    MAIN = int(input('Введите номер задания ИЛИ 0, если хотите завершить работу программы: '))
    if MAIN == 1:
        mid_k = input('K - середина ребра ').upper()
        div_m = input('M делит ребро ').upper()
        ratio = input('в отношении ')
        ratio = [int((ratio.replace(':', '/')).split('/')[i]) for i in range(2)]
        A = [0,0,0]
        B = [1,0,0]
        C = [1,1,0]
        D = [0,1,0]
        A1 = [0,0,1]
        B1 = [1,0,1]
        C1 = [1,1,1]
        D1 = [0,1,1]

        if mid_k.count('1') == 2:
            k1 = globals()[mid_k[:2]]
            k2 = globals()[mid_k[2:]]
        elif mid_k.count('1') == 0:
            k1 = globals()[mid_k[0]]
            k2 = globals()[mid_k[1]]
        elif mid_k.find('1') == 1:
            k1 = globals()[mid_k[:2]]
            k2 = globals()[mid_k[2]]
        else:
            k1 = globals()[mid_k[0]]
            k2 = globals()[mid_k[1:]]

        if div_m.count('1') == 2:
            m1 = globals()[div_m[:2]]
            m2 = globals()[div_m[2:]]
        elif div_m.count('1') == 0:
            m1 = globals()[div_m[0]]
            m2 = globals()[div_m[1]]
        elif div_m.find('1') == 1:
            m1 = globals()[div_m[:2]]
            m2 = globals()[div_m[2]]
        else:
            m1 = globals()[div_m[0]]
            m2 = globals()[div_m[1:]]
        n_ratio = ratio[0] / sum(ratio)
        K = [(k1[i] + k2[i]) / 2 for i in range(3)]
        M = [(m1[i]*(1 - n_ratio) + m2[i]*n_ratio) for i in range(3)]
        KM = [str(Fraction(M[i] - K[i]).limit_denominator()) for i in range(3)]
        if KM[1][0] != '-':
            KM[1] = '+' + KM[1]
        if KM[2][0] != '-':
            KM[2] = '+' + KM[2]
        print('KM = ', KM[0], 'a', KM[1], 'b', KM[2], 'c', sep='')
        input()


        
    if MAIN == 2:
        a = dots(input('Вектор a: '))
        b = dots(input('Вектор b: '))
        c = dots(input('Вектор c: '))
        d = dots(input('Вектор d: '))
        for i in range(3):
            a[i] = int(a[i])
            b[i] = int(b[i])
            c[i] = int(c[i])
            d[i] = int(d[i])
        D = np.dot(a, np.cross(b, c))
        Dx = np.dot(d, np.cross(b, c))
        Dy = np.dot(a, np.cross(d, c))
        Dz = np.dot(a, np.cross(b, d))
        print('Определитель для векторов a, b, c:', D, 'не равен 0')
        print('d = ', Dx//D, 'a', '{:+d}'.format(Dy//D), 'b', '{:+d}'.format(Dz//D), 'c', sep='')
        input()



    if MAIN == 3:
        def vect(sol):
            sol = ''.join(sol.split())
            loc_m = sol.find('m')
            loc_n = sol.find('n')
            if loc_m == -1:
                x = 0
            elif loc_m == 0:
                x = 1
            elif '-m' in sol:
                x = -1
            else:
                x = int(sol[0:loc_m])
            if loc_n == -1:
                y = 0
            elif '-n' in sol:
                y = -1
            elif '+n' in sol or sol[0] == 'n':
                y = 1
            else:
                y = int(sol[loc_m + 1:loc_n])
            return [x, y]

        a = vect(input('Вектор a = '))
        b = vect(input('Вектор b = '))
        ab_m = input('Длина вектора m = ')
        ab_n = input('Длина вектора n = ')
        ang_mn = input('Угол между m и n: ')

        for i in range(len(ab_m)):
            if i == 0:
                if 't(' in ab_m and ab_m[i] == 's':
                    break
                elif 't' in ab_m and not 't(' in ab_m:
                    ab_m = ab_m[:ab_m.find('t') + 1] + '(' + ab_m[ab_m.find('t') + 1:] + ')'
            elif ab_m[i] == 's' and ab_m[i-1] != '*':
                ab_m = ab_m[:i] + '*' + ab_m[i:]

        for i in range(len(ab_n)):
            if i == 0:
                if 't(' in ab_n and ab_n[i] == 's':
                    break
                elif 't' in ab_n and not 't(' in ab_n:
                    ab_n = ab_n[:ab_n.find('t') + 1] + '(' + ab_n[ab_n.find('t') + 1:] + ')'
            elif ab_n[i] == 's' and ab_n[i-1] != '*':
                ab_n = ab_n[:i] + '*' + ab_n[i:]

        for i in range(len(ang_mn)):
            if i == 0:
                if ang_mn == 'p':
                    break
            elif ang_mn[i] == 'p' and ang_mn[i-1] != '*':
                ang_mn = ang_mn[:i] + '*' + ang_mn[i:]

        ang_mn = simplify(ang_mn)
        ab_m = simplify(ab_m)
        ab_n = simplify(ab_n)
        mn_dot = ab_m*ab_n*cos(ang_mn)
        ax, ay, bx, by = a[0], a[1], b[0], b[1]
        ab_dot = ax*bx*ab_m**2 + (ax*by + ay*bx)*mn_dot + ay*by*ab_n**2
        a_dot = ax*ax*ab_m**2 + (ax*ay + ay*ax)*mn_dot + ay*ay*ab_n**2
        b_dot = bx*bx*ab_m**2 + (bx*by + by*bx)*mn_dot + by*by*ab_n**2
        print('cos(a,b) =', simplify(ab_dot / (sqrt(a_dot) * sqrt(b_dot))))
        print(mn_dot, ab_dot, a_dot, b_dot)
        input()


        
    if MAIN == 4:
        def vect(sol):
            sol = ''.join(sol.split())
            loc_a = sol.find('a')
            loc_b = sol.find('b')
            loc_c = sol.find('c')
            if loc_a == -1:
                A = 0
            elif loc_a == 0:
                A = 1
            elif '-a' in sol:
                A = -1
            else:
                A = int(sol[0:loc_a])
            if loc_b == -1:
                B = 0
            elif '-b' in sol:
                B = -1
            elif '+b' in sol or sol[0] == 'b':
                B = 1
            else:
                B = int(sol[loc_a + 1:loc_b])
            if loc_c == -1:
                C = 0
            elif '-c' in sol:
                C = -1
            elif '+c' in sol or sol[0] == 'c':
                C = 1
            else:
                C = int(sol[loc_b + 1:loc_c])
            return [A, B, C]


        x = vect(input('Вектор x: '))
        y = vect(input('Вектор y: '))
        a = dots(input('Вектор a: '))
        b = dots(input('Вектор b: '))
        c = dots(input('Вектор c: '))
        for i in range(3):
            a[i] = int(a[i])
            b[i] = int(b[i])
            c[i] = int(c[i])
        crd_x = [x[0]*a[i] + x[1]*b[i] + x[2]*c[i] for i in range(3)]
        crd_y = [y[0]*a[i] + y[1]*b[i] + y[2]*c[i] for i in range(3)]
        print(simplify(np.dot(crd_x, crd_y) / sqrt(crd_y[0]**2 + crd_y[1]**2 + crd_y[2]**2)))
        input()



    if MAIN == 5:
        A = dots(input('Точка A: '))
        B = dots(input('Точка B: '))
        C = dots(input('Точка C: '))
        for i in range(3):
            A[i] = int(A[i])
            B[i] = int(B[i])
            C[i] = int(C[i])

        AB = [B[i] - A[i] for i in range(3)]
        AC = [C[i] - A[i] for i in range(3)]
        n = np.cross(AB, AC)
        ab_n = sqrt(n[0]**2 + n[1]**2 + n[2]**2)
        print(AB, AC, n)
        print('Вектор n0 = +/-', [n[i] / ab_n for i in range(3)], sep='')
        input()


        
    if MAIN == 6:
        def vect(sol):
            sol = ''.join(sol.split())
            loc_m = sol.find('m')
            loc_n = sol.find('n')
            if loc_m == -1:
                x = 0
            elif loc_m == 0:
                x = 1
            elif '-m' in sol:
                x = -1
            else:
                x = int(sol[0:loc_m])
            if loc_n == -1:
                y = 0
            elif '-n' in sol:
                y = -1
            elif '+n' in sol or sol[0] == 'n':
                y = 1
            else:
                y = int(sol[loc_m + 1:loc_n])
            return [x, y]
        print('1. Площадь треугольника')
        print('2. Площадь параллелограмма')
        que = int(input('Выберите ваше задание: '))
        a = vect(input('Вектор a = '))
        b = vect(input('Вектор b = '))
        ab_m = input('Длина вектора m = ')
        ab_n = input('Длина вектора n = ')
        ang_mn = input('Угол между m и n: ')
        for i in range(len(ab_m)):
            if i == 0:
                if 't(' in ab_m and ab_m[i] == 's':
                    break
                elif 't' in ab_m and not 't(' in ab_m:
                    ab_m = ab_m[:ab_m.find('t') + 1] + '(' + ab_m[ab_m.find('t') + 1:] + ')'
            elif ab_m[i] == 's' and ab_m[i-1] != '*':
                ab_m = ab_m[:i] + '*' + ab_m[i:]
        for i in range(len(ab_n)):
            if i == 0:
                if 't(' in ab_n and ab_n[i] == 's':
                    break
                elif 't' in ab_n and not 't(' in ab_n:
                    ab_n = ab_n[:ab_n.find('t') + 1] + '(' + ab_n[ab_n.find('t') + 1:] + ')'
            elif ab_n[i] == 's' and ab_n[i-1] != '*':
                ab_n = ab_n[:i] + '*' + ab_n[i:]
        for i in range(len(ang_mn)):
            if i == 0:
                if ang_mn == 'p':
                    break
            elif ang_mn[i] == 'p' and ang_mn[i-1] != '*':
                ang_mn = ang_mn[:i] + '*' + ang_mn[i:]


        ang_mn = simplify(ang_mn)
        ab_m = simplify(ab_m)
        ab_n = simplify(ab_n)
        mn_cross = ab_m*ab_n*sin(ang_mn)
        ax, ay, bx, by = a[0], a[1], b[0], b[1]
        ab_dot = abs(ax*by - ay*bx)*mn_cross
        print('S(ab) =', ab_dot*que/2)
        input()


        
    if MAIN == 7:
        a = dots(input('Вектор a = '))
        b = dots(input('Вектор b = '))
        c = dots(input('Вектор c = '))
        for i in range(3):
            a[i] = int(a[i])
            b[i] = int(b[i])
            c[i] = int(c[i])
        if np.dot(a, np.cross(b, c)) == 0:
            print('Векторы компланарны. det = 0')
        else:
            print('Векторы некомпланарны. det =', np.dot(a, np.cross(b, c)))
        input()

            
    if MAIN == 8:
        print('1. Объём тетраэдра')
        print('2. Объём параллепипеда')
        que = int(input('Выберите, что нужно вычислить: '))
        H = dots(input('Координаты точки, из которой проведена высота: '))
        print('Введите остальные данные точки')
        A = dots(input('Точка 1: '))
        B = dots(input('Точка 2: '))
        C = dots(input('Точка 3: '))
        a = [int(B[i]) - int(A[i]) for i in range(3)]
        b = [int(C[i]) - int(A[i]) for i in range(3)]
        c = [int(H[i]) - int(A[i]) for i in range(3)]
        print(a, b, c)
        V = abs(np.dot(a, np.cross(b, c))*(1/(-5*que+11)))
        print('V =', simplify(V))
        v_ab = np.cross(a, b)
        print(v_ab)
        S = sqrt(v_ab[0]**2 + v_ab[1]**2 + v_ab[2]**2)*(1/(3-que))
        print('S =', simplify(S))
        with evaluate(False):
            print(V/S)
        print(V/S)
        h = (V/S)*(-2*que+5)
        print('h =', simplify(h))
        input()


        
    if MAIN == 9:
        print('Общий вид уравнения плоскости!')
        a = input('Уравнение плоскости 1: ')
        b = input('Уравнение плоскости 2: ')
        S_a = flat(a)
        S_b = flat(b)
        A1 = S_a[0]
        B1 = S_a[1]
        C1 = S_a[2]
        D1 = S_a[3]
        A2 = S_b[0]
        B2 = S_b[1]
        C2 = S_b[2]
        D2 = S_b[3]
        print(S_a, S_b, np.dot(S_a, S_b))
        print('cos(a,b) =', abs(A1*A2 + B1*B2 + C1*C2) / ((sqrt(A1**2 + B1**2 + C1**2)) * (sqrt(A2**2 + B2**2 + C2**2))))
        input()

        

    if MAIN == 10:
        x, y, z, ro = symbols('x y z ro')
        print('Формат ввода: x0;y0;z0')

        A = dots(input('Точка A: '))
        B = dots(input('Точка B: '))
        C = dots(input('Точка C: '))
        S = dots(input('Точка S: '))
        AB = [int(B[i]) - int(A[i]) for i in range(len(A))]
        AC = [int(C[i]) - int(A[i]) for i in range(len(A))]
        v_cr = np.cross(AB, AC)
        GCD = np.gcd.reduce(v_cr)
        al = v_cr[0] // GCD
        be = v_cr[1] // GCD
        ga = v_cr[2] // GCD
        de = -(int(A[0])*al+int(A[1])*be+int(A[2])*ga)
        print('a: ', al, 'x', "{:+d}".format(be), 'y', "{:+d}".format(ga), 'z',
              "{:+d}".format(-(int(A[0])*al+int(A[1])*be+int(A[2])*ga)), '=0', sep='')

        equation = [Eq(ga, v_cr[2] // GCD), Eq(abs(al*int(S[0]) + be*int(S[1]) + ga*int(S[2]) + de) / (sqrt(al**2+be**2+ga**2)), ro)]
        solution = solve(equation, ro)   
        print('Расстояние =', solution[ro])
        print((abs(al*int(S[0]) + be*int(S[1]) + ga*int(S[2]) + de)) / (sqrt(al**2 + be**2 + ga**2)))
        input()

        
        
        
    if MAIN == 11:
        print('Прямые вводить в каноническом виде, плоскости в общем виде')
        print('1. Уравнение плоскости, параллельной 2 прямым')
        print('2. Уравнение плоскости, перпендикулярной 2 плоскостям')
        print('3. Уравнение плоскости, перпендикулярной плоскости и параллельной прямой')
        print('4. Уравнения прямой, параллельной плоскости и перпендикулярной прямой')
        THE = int(input('Введите номер задачи (из данных): '))

        M = dots(input('Точка: '))
        if THE == 1:
            a = input('Прямая 1: ')
            b = input('Прямая 2: ')
            S_a = line(a)
            S_b = line(b)
            v_a = [int(S_a[1][0]), int(S_a[1][1]), int(S_a[1][2])]
            v_b = [int(S_b[1][0]), int(S_b[1][1]), int(S_b[1][2])]
            V = np.cross(v_a, v_b)
            A = V[0]
            B = V[1]
            C = V[2]
            D = -(A*int(M[0]) + B*int(M[1]) + C*int(M[2]))
            print('a: ', A, 'x', '{:+d}'.format(B), 'y', '{:+d}'.format(C), 'z', '{:+d}'.format(D), '=0', sep='')

        if THE == 2:
            a = input('Плоскость 1: ')
            b = input('Плоскость 2: ')
            S_a = flat(a)
            S_b = flat(b)
            v_a = [int(S_a[0]), int(S_a[1]), int(S_a[2])]
            v_b = [int(S_b[0]), int(S_b[1]), int(S_b[2])]
            V = np.cross(v_a, v_b)
            A = V[0]
            B = V[1]
            C = V[2]
            D = -(A*int(M[0]) + B*int(M[1]) + C*int(M[2]))
            print('a: ', A, 'x', '{:+d}'.format(B), 'y', '{:+d}'.format(C), 'z', '{:+d}'.format(D), '=0', sep='')

        if THE == 3:
            a = input('Плоскость: ')
            b = input('Прямая: ')
            S_a = flat(a)
            S_b = line(b)
            v_a = [int(S_a[0]), int(S_a[1]), int(S_a[2])]
            v_b = [int(S_b[1][0]), int(S_b[1][1]), int(S_b[1][2])]
            V = np.cross(v_a, v_b)
            A = V[0]
            B = V[1]
            C = V[2]
            D = -(A*int(M[0]) + B*int(M[1]) + C*int(M[2]))
            print('a: ', A, 'x', '{:+d}'.format(B), 'y', '{:+d}'.format(C), 'z', '{:+d}'.format(D), '=0', sep='')

        if THE == 4:
            a = input('Плоскость: ')
            b = input('Прямая: ')
            S_a = flat(a)
            S_b = line(b)
            v_a = [int(S_a[0]), int(S_a[1]), int(S_a[2])]
            v_b = [int(S_b[1][0]), int(S_b[1][1]), int(S_b[1][2])]
            V = np.cross(v_a, v_b)
            p = V[0]
            q = V[1]
            r = V[2]
            if (str(p) + str(q) + str(r)).count('-') >= 2:
                p, q, r = -p, -q, -r
            print('l: (x', '{:+d}'.format(-int(M[0])), ')/', p, ' = (y', '{:+d}'.format(-int(M[1])), ')/', q, ' = (z', '{:+d}'.format(-int(M[2])), ')/', r, sep = '')
        input()


        
    if MAIN == 12:
        x, y, z, ro = symbols('x y z ro')
        print('Формат ввода: x0;y0;z0')

        A = dots(input('Точка A: '))
        B = dots(input('Точка B: '))
        C = dots(input('Точка С: '))

        s = [int(B[i]) - int(A[i]) for i in range(3)]
        if (str(s[0]) + str(s[1]) + str(s[2])).count('-') >= 2:
            s[0], s[1], s[2] = -s[0], -s[1], -s[2]
        print('l: (', simplify(f'{x}-{A[0]}'), ')/', s[0], ' = ',
              '(', simplify(f'{y}-{A[1]}'), ')/', s[1], ' = ',
              '(', simplify(f'{z}-{A[2]}'), ')/', s[2], sep='')
        h = [int(C[i]) - int(A[i]) for i in range(3)]
        cr = np.cross(s,h)
        print('Расстояние =', simplify((sqrt(cr[0]**2 + cr[1]**2 + cr[2]**2)) / (sqrt(s[0]**2 + s[1]**2 + s[2]**2))))
        input()



    if MAIN == 13:
        x, y, z, ro = symbols('x y z ro')
        print('Общий вид уравнения плоскости!')
        a = input('Уравнение плоскости 1: ')
        b = input('Уравнение плоскости 2: ')
        S_a = flat(a)
        S_b = flat(b)
        A1, B1, C1, D1 = S_a[0], S_a[1], S_a[2], S_a[3]
        A2, B2, C2, D2 = S_b[0], S_b[1], S_b[2], S_b[3]
                
        a_n = [A1,B1,C1]
        b_n = [A2,B2,C2]
        cross = np.cross(a_n, b_n)
        if (str(cross[0]) + str(cross[1]) + str(cross[2])).count('-') >= 2:
            cross[0], cross[1], cross[2] = -cross[0], -cross[1], -cross[2]
        if B1 != B2 and C1 != C2:
            equation = [Eq(A1*x+C1*z+D1, 0), Eq(A2*x+C2*z+D2, 0)]
            ans = solve(equation, (x,z))
            print('l: (', simplify(x - ans.get(x)), ')/', cross[0], ' = y/', cross[1], ' = (', simplify(z-ans.get(z)), ')/', cross[2], sep = '')
        elif B1 == B2 and A1 != A2:
            equation = [Eq(B1*y+C1*z+D1, 0), Eq(B2*y+C2*z+D2, 0)]
            ans = solve(equation, (y,z))
            print('l: x/', cross[0], '= (', simplify(y - ans.get(y)), ')/', cross[1], ' = (', simplify(z-ans.get(z)), ')/', cross[2], sep = '')
        else:
            equation = [Eq(B1*y+A1*x+D1, 0), Eq(B2*y+A2*x+D2, 0)]
            ans = solve(equation, (x,y))
            print('l: (', simplify(x - ans.get(x)), ')/', cross[0], '= (', simplify(y - ans.get(y)), ')/', cross[1], ' = z/', cross[2], sep = '')
        input()


        
    if MAIN == 14:
        x, y, z, t = symbols('x y z t')

        print('1. Проекция на плоскость')
        print('2. Точка, зеркальная данной')
        que = int(input())
        print('\n', 'Плоскость задаётся общим уравнением. Точка вводится как x;y;z', sep = '')
        M = dots(input('Точка: '))
        p = flat(input('Плоскость: '))
        A = p[0]
        B = p[1]
        C = p[2]
        D = p[3]
        x0 = int(M[0])
        y0 = int(M[1])
        z0 = int(M[2])
        equation = Eq(A*(x0+A*t)+B*(y0+B*t)+C*(z0+C*t)+D, 0)
        t0 = solve(equation, t)[0]
        print('M1 = (',x0+A*que*t0, ';', y0+B*que*t0, ';', z0+C*que*t0, ')', sep='')
        input()


        
    if MAIN == 15:
        print('Уравнение прямой в каноническом виде x-x0/p=y-y0/q=z-z0/r без скобок')
        print('Уравнение плоскости в общем виде')
        m = input('Уравнение прямой: ')
        a = input('Уравнение плоскости: ')
        S_a = flat(a)
        S_m = line(m)
        A, B, C = S_a[0], S_a[1], S_a[2]
        p, q, r = S_m[1][0], S_m[1][1], S_m[1][2]

        vect1 = [p, q, r]
        vect2 = [A, B, C]
        print('Угол =', simplify(asin(abs(np.dot(vect1, vect2)) / (sqrt(A**2 + B**2 + C**2) * sqrt(p*p+q*q+r*r)))))
        input()
