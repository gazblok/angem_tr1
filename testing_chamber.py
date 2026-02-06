from solver import *
from generator import *
from validator import *
from local_functions import *
from model_task import *
from model_solution import *

a = generate(2)
valid(Answer(answer=solvers(a), task=a))