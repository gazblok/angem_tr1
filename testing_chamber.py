from solver import *
from generator import *
from validator import *
from local_functions import *
from model_task import *
from model_solution import *

a = gen_task5()
print(a)
print(solve_task5(a))
print(valid_task5(user_inp))