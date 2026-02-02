def flat(sol):
    sol = ''.join(sol.split())
    loc_x = sol.find('x')
    loc_y = sol.find('y')
    loc_z = sol.find('z')
    if loc_x == -1:
        A = 0
    elif loc_x == 0:
        A = 1
    elif '-x' in sol:
        A = -1
    else:
        A = int(sol[0:loc_x])
    if loc_y == -1:
        B = 0
    elif '-y' in sol:
        B = -1
    elif '+y' in sol or sol[0] == 'y':
        B = 1
    else:
        B = int(sol[loc_x + 1:loc_y])
    if loc_z == -1:
        C = 0
    elif '-z' in sol:
        C = -1
    elif '+z' in sol or sol[0] == 'z':
        C = 1
    else:
        C = int(sol[loc_y + 1:loc_z])
    if max(loc_x, loc_y, loc_z) + 1 == sol.find('=') and '=0' in sol:
        D = 0
    elif '=0' in sol:
        D = int(sol[max(loc_x, loc_y, loc_z) + 1:sol.find('=')])
    else:
        D = -int(sol[sol.find('=') + 1:])
    return [A, B, C, D]

def dots(d):
    divide = ' '
    flag = False
    for i in range(len(d)):
        if d[i].isdigit() or d[i] == '-':
            break
    for k in range(len(d)):
        if not (d[k].isdigit() or d[k] == '-' or d[k] == ' '):
            flag = True
            break
    d = d[i:]
    for j in range(len(d)):
        if d[j].isdigit():
            max_j = j
    d = d[:max_j + 1]
    d = d.strip()
    if not flag:
        return d.split(' ')
    elif ''.join(d.split(' ')).isdigit():
        d = d.split(' ')
        x0 = d[0]
        y0 = d[1]
        z0 = d[2]
        return [x0, y0, z0]
    else:
        d = ''.join(d.split(' '))
        for i in range(len(d)):
            if not d[i].isdigit() and d[i] != '-':
                divide = d[i]
                break
        d = d.split(divide)
        x0 = d[0]
        y0 = d[1]
        z0 = d[2]
        return [x0, y0, z0]

def line(sol):
    loc_x = sol.find('x')
    loc_y = sol.find('y')
    loc_z = sol.find('z')
    c = 0
    temp_i = 0
    sol = ''.join(sol.split())
    sol = ''.join(sol.split('('))
    sol = ''.join(sol.split(')'))
    for i in range(len(sol)):
        flag = True
        if c == 0 and sol[i] == '/' and loc_x + 1 < i:
            x0 = -int(sol[loc_x + 1:i])
            temp_i = i
        elif c == 0 and sol[i] == '/':
            x0 = 0
            temp_i = i
        if c == 0 and sol[i] == '=':
            c = 1
            p = int(sol[temp_i + 1:i])
            flag = False
        if c == 1 and sol[i] == '/' and loc_y + 1 < i:
            y0 = -int(sol[loc_y + 1:i])
            temp_i = i
        elif c == 1 and sol[i] == '/':
            y0 = 0
            temp_i = i
        if c == 1 and sol[i] == '=' and flag:
            c = 2
            q = int(sol[temp_i + 1:i])
            flag = False
        if c == 2 and sol[i] == '/' and loc_z + 1 < i:
            z0 = -int(sol[loc_z + 1:i])
            temp_i = i
            r = int(sol[i + 1:])
        elif c == 2 and sol[i] == '/':
            z0 = 0
            r = int(sol[i + 1:])
    return [[x0, y0, z0], [p, q, r]]