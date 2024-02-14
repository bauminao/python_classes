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
print ("Abaqus - Objekt")
ABQ_OBJ = Solver.selectSolver(meta)

print ("Abaqus - common-function aus Solver: ", end='')
ABQ_OBJ.common_func()

print ("Abaqus - overwritten function: ", end='')
ABQ_OBJ.common_func_overwrite()

print ("Abaqus - child-spezifische Funktion: ", end='')
ABQ_OBJ.abq_func()

print ("Abaqus - but base-class overwritten function: ", end='')
ABQ_OBJ.common_func_overwrite_BASE()
print ("")
