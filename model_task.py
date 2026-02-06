from typing import Optional
from pydantic import BaseModel

class Task(BaseModel):
    task_code_number: int
    class Task1(BaseModel):
        '''
        K - середина отрезка K_start-K_end
        M - делит в отношении M_top:M_bottom отрезок M_start-M_end
        '''
        task_code_number: int
        K_start: str
        K_end: str
        M_top: int
        M_bottom: int
        M_start: str
        M_end: str

    class Task2(BaseModel):
        '''
        Найти разложение вектора d по векторам a, b, c
        '''
        task_code_number: int
        a: list
        b: list
        c: list
        d: list

    class Task3(BaseModel):
        '''
        Найти косинус угла между a = a_m*m + a_n*n и b = b_m*m + b_n*n,
        если |m|=len_m, |n|=len_n, угол(m;n)=angle
        '''
        task_code_number: int
        a_m: int
        a_n: int
        b_m: int
        b_n: int
        len_m: str
        len_n: str
        angle: str

    class Task4(BaseModel):
        '''
        Найти проекцию x на y, если x и y -
        ЛК векторов a,b,c
        '''
        task_code_number: int
        x_a: int
        x_b: int
        x_c: int
        y_a: int
        y_b: int
        y_c: int
        a: list
        b: list
        c: list

    class Task5(BaseModel):
        '''
        Найти единичный вектор n0, перпендикулярный плоскости ABC
        '''
        task_code_number: int
        A: list
        B: list
        C: list
    
    class Task6(BaseModel):
        '''
        Найти площадь (1. треугольника / 2. параллелограмма)
        на векторах a, b - ЛК m, n; если |m|=len_m,
        |n|=len_n, угол (m;n) = angle
        '''
        task_code_number: int
        subtask: int
        a_m: int
        a_n: int
        b_m: int
        b_n: int
        len_m: int
        len_n: int
        angle: str

    class Task7(BaseModel):
        '''
        Компланарны ли векторы a b c ИЛИ
        Лежат ли в одной плоскости точки A B C D?
        '''
        task_code_number: int
        subtask: int
        A: list
        B: list
        C: list
        D: list
        a: list
        b: list
        c: list
    
    class Task8(BaseModel):
        '''
        Вычислить объём, площадь грани ABC и высоту к ней 
        из точки H фигуры при данных её 4 точках A, B, C, H
        '''
        task_code_number: int
        subtask: int
        A: list
        B: list
        C: list
        H: list

    class Task9(BaseModel):
        '''
        Найти косинус угла между плоскостями
        A1x+B1y+C1z+D1=0 и A2x+B2y+C2z+D2=0
        '''
        task_code_number: int
        A1: int
        B1: int
        C1: int
        D1: int
        A2: int
        B2: int
        C2: int
        D2: int
    class Task10(BaseModel):
        task_code_number: int
        A: list
        B: list
        C: list
        S: list
