from typing import Optional, Union
from pydantic import BaseModel
from model_task import *

class Solution(BaseModel):
    class Solution_Task1(BaseModel):
        '''
        Вектор с координатами в базисе (a b c)
        '''
        KM_a: Optional[str] = ''
        KM_b: Optional[str] = ''
        KM_c: Optional[str] = ''
    class Solution_Task2(BaseModel):
        '''
        Вектор d с координатами в базисе (a b c)
        '''
        d_a: Optional[int] = 0
        d_b: Optional[int] = 0
        d_c: Optional[int] = 0
    class Solution_Task3(BaseModel):
        '''
        Косинус угла между веторами
        '''
        answer: Optional[str] = ''
    class Solution_Task4(BaseModel):
        '''
        Проекция вектора на другой вектор (число)
        '''
        answer: Optional[str] = ''
    class Solution_Task5(BaseModel):
        '''
        Координаты единичного вектора
        '''
        n0_x: Optional[str] = ''
        n0_y: Optional[str] = ''
        n0_z: Optional[str] = ''
    class Solution_Task6(BaseModel):
        '''
        Площадь фигуры
        '''
        answer: Optional[str] = ''
    class Solution_Task7(BaseModel):
        '''
        Комаланарны ли (да/нет) и определитель
        '''
        answer: Optional[bool] = False
        det: Optional[int] = 0
    class Solution_Task8(BaseModel):
        '''
        Объём, площадь грани, высота
        '''
        Volume: Optional[str] = ''
        Surf_area: Optional[str] = ''
        height: Optional[str] = ''
    class Solution_Task9(BaseModel):
        '''
        Косинус угла
        '''
        answer: Optional[str] = ''
    class Solution_Task10(BaseModel):
        '''
        Составить уравнение плоскости,
        найти расстояние от S до ABC
        '''
        surf_a: Optional[int] = 0
        surf_b: Optional[int] = 0
        surf_c: Optional[int] = 0
        surf_d: Optional[int] = 0
        distance: Optional[str] = ''

class Answer(BaseModel):
    task: Union[Task.Task1, Task.Task2, Task.Task3, Task.Task4, Task.Task5, Task.Task6, Task.Task7, Task.Task8,
                Task.Task9, Task.Task10]
    answer: Union[Solution.Solution_Task1, Solution.Solution_Task2, Solution.Solution_Task3, Solution.Solution_Task4,
                  Solution.Solution_Task5, Solution.Solution_Task6, Solution.Solution_Task7, Solution.Solution_Task8,
                  Solution.Solution_Task9, Solution.Solution_Task10]
