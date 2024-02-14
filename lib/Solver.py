import os

def selectSolver(solvobj):
  return Abaqus()


class Solver:
  def __init__(self,submitscript="",scriptdir=os.path.dirname(os.path.realpath(__file__))):
    self.solvervar  = "default"
    print ("Init in Solver")

  def common_func(self):
    print ("Solver - Allgemeine Funktion")

  def common_func_overwrite(self):
    print ("Solver - Overwrite, Basisklasse")


class Abaqus(Solver):
  def __init__(self):
    print ("Init in Abaqus")
  def abq_func(self):
    print ("Abaqus - ABQ-Funktion")
  def common_func_overwrite(self):
    print ("Abaqus - Overwrite, Child-Klasse")





