import os
import sys
import random
import variables

sys.path.append(".")

from lists import List
from fractions import Fraction

fraction_division_file = open("fraction-division.tex", "a")
fraction_division_spanish_file = open("fraction-division-spanish.tex", "a")
fraction_division_sol_file = open("fraction-division-sol.tex", "a")

fraction_division_file.write(r"\documentclass{article}")
fraction_division_spanish_file.write(r"\documentclass{article}")
fraction_division_sol_file.write(r"\documentclass{article}")

fraction_division_file.write("\n\n")
fraction_division_spanish_file.write("\n\n")
fraction_division_sol_file.write("\n\n")

fraction_division_file.write(r"\usepackage{amsmath}")
fraction_division_spanish_file.write(r"\usepackage{amsmath}")
fraction_division_sol_file.write(r"\usepackage{amsmath}")

fraction_division_file.write("\n\n")
fraction_division_spanish_file.write("\n\n")
fraction_division_sol_file.write("\n\n")

fraction_division_file.write(r"\usepackage[utf8]{inputenc}")
fraction_division_spanish_file.write(r"\usepackage[utf8]{inputenc}")
fraction_division_sol_file.write(r"\usepackage[utf8]{inputenc}")

fraction_division_file.write("\n\n")
fraction_division_spanish_file.write("\n\n")
fraction_division_sol_file.write("\n\n")

fraction_division_file.write(r"\begin{document}")
fraction_division_spanish_file.write(r"\begin{document}")
fraction_division_sol_file.write(r"\begin{document}")

fraction_division_file.write("\n\n")
fraction_division_spanish_file.write("\n\n")
fraction_division_sol_file.write("\n\n")

fraction_division_file.write(r"\begin{verbatim}")
fraction_division_spanish_file.write(r"\begin{verbatim}")

fraction_division_file.write("\n\n")
fraction_division_spanish_file.write("\n\n")

fraction_division_file.write(variables.banner_2)
fraction_division_spanish_file.write(variables.spanish_banner_2)

fraction_division_file.write("\n\n")
fraction_division_spanish_file.write("\n\n")

fraction_division_file.write(r"\end{verbatim}")
fraction_division_spanish_file.write(r"\end{verbatim}")

fraction_division_file.write("\n\n")
fraction_division_spanish_file.write("\n\n")

rand = List

for problem in range(1, 101):
    numerator_1 = random.choice(rand.random_list())
    numerator_2 = random.choice(rand.random_list())
    denominator_1 = random.choice(rand.random_list())
    denominator_2 = random.choice(rand.random_list())

    new_problem = Fraction(numerator_1, numerator_2, denominator_1, denominator_2)

    fraction_division_file.write(f"Problem {problem}\n")
    fraction_division_spanish_file.write(f"Problem {problem}\n")
    fraction_division_sol_file.write(f"Problem {problem}\n")

    fraction_division_file.write(r"\newline")
    fraction_division_spanish_file.write(r"\newline")
    fraction_division_sol_file.write(r"\newline")

    fraction_division_file.write("\n")
    fraction_division_spanish_file.write("\n")
    fraction_division_sol_file.write("\n")

    fraction_division_file.write(r"\hfill \break")
    fraction_division_spanish_file.write(r"\hfill \break")
    fraction_division_sol_file.write(r"\hfill \break")

    fraction_division_file.write("\n")
    fraction_division_spanish_file.write("\n")
    fraction_division_sol_file.write("\n")

    fraction_division_file.write(r"$\displaystyle \frac{")
    fraction_division_spanish_file.write(r"$\displaystyle \frac{")

    fraction_division_file.write(f"{numerator_1}")
    fraction_division_spanish_file.write(f"{numerator_1}")

    fraction_division_file.write(r"}{")
    fraction_division_spanish_file.write(r"}{")

    fraction_division_file.write(f"{denominator_1}")
    fraction_division_spanish_file.write(f"{denominator_1}")

    fraction_division_file.write(r"} \div \frac{")
    fraction_division_spanish_file.write(r"} \div \frac{")

    fraction_division_file.write(f"{numerator_2}")
    fraction_division_spanish_file.write(f"{numerator_2}")

    fraction_division_file.write(r"}{")
    fraction_division_spanish_file.write(r"}{")

    fraction_division_file.write(f"{denominator_2}")
    fraction_division_spanish_file.write(f"{denominator_2}")

    fraction_division_file.write(r"}$")
    fraction_division_spanish_file.write(r"}$")

    fraction_division_file.write("\n")
    fraction_division_spanish_file.write("\n")

    fraction_division_file.write(r"\newline")
    fraction_division_spanish_file.write(r"\newline")

    fraction_division_file.write("\n")
    fraction_division_spanish_file.write("\n")

    fraction_division_file.write(r"\hfill \break")
    fraction_division_spanish_file.write(r"\hfill \break")

    fraction_division_file.write("\n")
    fraction_division_spanish_file.write("\n")

    fraction_division_sol_file.write(r"$\displaystyle \frac{")
    fraction_division_sol_file.write(f"{new_problem.reduced_numerator()}")
    fraction_division_sol_file.write(r"}{")
    fraction_division_sol_file.write(f"{new_problem.reduced_denominator()}")
    fraction_division_sol_file.write(r"}$")
    fraction_division_sol_file.write("\n")
    fraction_division_sol_file.write(r"\newline")
    fraction_division_sol_file.write("\n")
    fraction_division_sol_file.write("\hfill \break")
    fraction_division_sol_file.write("\n")

fraction_division_file.close()
fraction_division_spanish_file.close()
fraction_division_sol_file.close()
