import os
import sys
import random

sys.path.append(".")

from lists import List
from functions import Function

sin_cos_tan = open("sin-cos-tan.md", "a")
sin_cos_tan_spanish = open("sin-cos-tan-spanish.md", "a")
sin_cos_tan_sol = open("sin-cos-tan-sol.md", "a")

rand = List

sin_cos_tan.write("Name: ________________________\n\n")
sin_cos_tan.write("Date: ________________________\n\n")

sin_cos_tan_spanish.write("Nombre: ________________________\n\n")
sin_cos_tan_spanish.write("Fecha: ________________________\n\n")

sin_cos_tan.write("Find the following trig values, round to 3 decimal places if necessary.\n\n")
sin_cos_tan_spanish.write("Encuentre los siguientes valores trigonométricos, redondee a 3 lugares decimales si es necesario.\n\n")

for problem in range(1, 101):
    degrees = random.choice(rand.random_list())
    problem_type = random.choice(rand.problem_type_list())

    new_problem = Function(degrees)

    sin_cos_tan.write(f"Problem {problem}\n\n")
    sin_cos_tan_spanish.write(f"Problema {problem}\n\n")
    sin_cos_tan_sol.write(f"Problem {problem}\n\n")

    if problem_type == 1:
        sin_cos_tan.write(f"sin({degrees}&deg;) = \n\n")
        sin_cos_tan_spanish.write(f"sin({degrees}&deg;) = \n\n")
        sin_cos_tan_sol.write(f"Solution: {round(new_problem.sin_solution(), 3)}\n\n")
    elif problem_type == 2:
        sin_cos_tan.write(f"cos({degrees}&deg;) = \n\n")
        sin_cos_tan_spanish.write(f"cos({degrees}&deg;) = \n\n")
        sin_cos_tan_sol.write(f"Solution: {round(new_problem.cos_solution(), 3)}\n\n")
    else:
        if degrees == 90 or degrees == 270:
            sin_cos_tan.write(f"tan({degrees}&deg;) = \n\n")
            sin_cos_tan_spanish.write(f"tan({degrees}&deg;) = \n\n")
            sin_cos_tan_sol.write("The value is undefined.\n\n")
        else:
            sin_cos_tan.write(f"tan({degrees}&deg;) = \n\n")
            sin_cos_tan_spanish.write(f"tan({degrees}&deg;) = \n\n")
            sin_cos_tan_sol.write(f"Solution: {round(new_problem.tan_solution(), 3)}\n\n")

    sin_cos_tan.write("---\n\n")
    sin_cos_tan_spanish.write("---\n\n")
    sin_cos_tan_sol.write("---\n\n")

sin_cos_tan.close()
sin_cos_tan_spanish.close()
sin_cos_tan_sol.close()
