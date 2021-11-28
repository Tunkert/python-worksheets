class Function:
    def __init__(self, coeff_1, const_1):
        self.coeff_1 = coeff_1
        self.const_1 = const_1

    def fOfXString(self):
        fFuncString = f"{self.coeff_1}x + {self.const_1}"
        return fFuncString

    def solutionString(self):
        solution = r"\["
        solution += "\n"
        solution += r"f^{-1}(x) = "
        solution += r"\frac{"
        solution += f"x - {self.const_1}"
        solution += r"}{"
        solution += f"{self.coeff_1}"
        solution += r"}"
        solution += "\n"
        solution += r"\]"
        return solution
