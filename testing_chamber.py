from solver import *
from generator import *
from validator import *
from local_functions import *
from model_task import *
from model_solution import *

for j in range(1,10):
    for i in range(100):
        a = generate(j)
        print(solvers(a))