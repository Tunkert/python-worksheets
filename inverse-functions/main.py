import os
import sys
import random

sys.path.append(".")

from lists import List
from functions import Function

rand = List

inverse_functions_file = open("inverse-functions.md", "a")
inverse_functions_spanish_file = open("inverse-functions-spanish.md", "a")
inverse_functions_sol_file = open("inverse-functions-sol.tex", "a")

inverse_functions_sol_file.write(r"\documentclass{article}")
inverse_functions_sol_file.write("\n\n")
inverse_functions_sol_file.write(r"\usepackage{amsmath}")
inverse_functions_sol_file.write("\n\n")
inverse_functions_sol_file.write(r"\begin{document}")
inverse_functions_sol_file.write("\n\n")

for problem in range(1, 101):
    coeff_1 = random.choice(rand.random_list())
    const_1 = random.choice(rand.random_list())

    new_problem = Function(coeff_1, const_1)

    inverse_functions_file.write(f"Problem {problem}\n\n")
    inverse_functions_spanish_file.write(f"Problem {problem}\n\n")
    inverse_functions_sol_file.write(f"Problem {problem}\n\n")

    inverse_functions_file.write("What is the inverse function of f(x) if ")
    inverse_functions_file.write(f"f(x) = {new_problem.fOfXString()}?\n\n")
    inverse_functions_spanish_file.write("¿Cuál es la función inversa de f(x)")
    inverse_functions_spanish_file.write(f" si f(x) = {new_problem.fOfXString()}?\n\n")

    inverse_functions_sol_file.write(f"{new_problem.solutionString()}\n\n")

    inverse_functions_file.write("---\n\n")
    inverse_functions_spanish_file.write("---\n\n")

inverse_functions_sol_file.write(r"\end{document}")
inverse_functions_file.close()
inverse_functions_spanish_file.close()
inverse_functions_sol_file.close()
