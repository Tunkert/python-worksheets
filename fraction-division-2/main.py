import os
import sys
import random
import variables

sys.path.append(".")

from lists import List
from fractions import Fraction

rand = List

fraction_div_file = open("fraction-div-file.html", "a")
fraction_div_spanish_file = open("fraction-div-spanish-file.html", "a")
fraction_div_sol_file = open("fraction-div-sol-file.html", "a")

# fraction_div_file.write("<pre>\n")
# fraction_div_file.write(variables.banner)
# fraction_div_file.write("\n")
# fraction_div_file.write("</pre>\n")

# fraction_div_spanish_file.write("<pre>\n")
# fraction_div_spanish_file.write(variables.spanish_banner)
# fraction_div_spanish_file.write("\n")
# fraction_div_spanish_file.write("</pre>\n")

fraction_div_sol_file.write("<h1>Solutions</h1>\n")

for problem in range(1, 101):
    numerator_1 = random.choice(rand.random_list())
    numerator_2 = random.choice(rand.random_list())
    denominator_1 = random.choice(rand.random_list())
    denominator_2 = random.choice(rand.random_list())

    new_problem = Fraction(numerator_1, numerator_2, denominator_1, denominator_2)

    fraction_div_file.write(f"<h2>Problem {problem}</h2>\n")
    fraction_div_spanish_file.write(f"<h2>Problem {problem}</h2>\n")
    fraction_div_sol_file.write(f"<h2>Problem {problem}</h2>\n")

    fraction_div_file.write(f"<p><sup>{numerator_1}</sup>/<sub>{denominator_1}</sub> ")
    fraction_div_file.write(f"&div; <sup>{numerator_2}</sup>/<sub>{denominator_2}</sub> = </p>\n")

    fraction_div_spanish_file.write(f"<p><sup>{numerator_1}</sup>/<sub>{denominator_1}</sub> ")
    fraction_div_spanish_file.write(f"&div; <sup>{numerator_2}</sup>/<sub>{denominator_2}</sub> = </p>\n")

    fraction_div_sol_file.write(f"<p>Solution: <sup>{new_problem.reduced_numerator()}</sup>/")
    fraction_div_sol_file.write(f"<sub>{new_problem.reduced_denominator()}</sub></p>\n")

    fraction_div_file.write("<hr />\n")
    fraction_div_spanish_file.write("<hr />\n")
    fraction_div_sol_file.write("<hr />\n")

fraction_div_file.close()
fraction_div_spanish_file.close()
fraction_div_sol_file.close()
