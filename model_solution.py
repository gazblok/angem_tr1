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


class Answer(BaseModel):
    task_num: int
    task: Union[Task.Task1, Task.Task2, Task.Task3, Task.Task4, Task.Task5]
    answer: Union[Solution.Solution_Task1, Solution.Solution_Task2, Solution.Solution_Task3, Solution.Solution_Task4, Solution.Solution_Task5]
