#!/bin/env python3 

import os
from lib import Solver


print ("MAIN - Solverkrams")
print ("==================")
print ("")

meta = Solver.Solver(submitscript=os.path.basename(__file__))
meta.common_func()
meta.common_func_overwrite()
#meta.abq_func()              # Die gibt es hier natürlich noch nicht.


print ("")
ABQ_OBJ = Solver.selectSolver(meta)

ABQ_OBJ.common_func()
ABQ_OBJ.common_func_overwrite()
ABQ_OBJ.abq_func()

print ("")
