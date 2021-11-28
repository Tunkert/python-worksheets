import math

class Function:
    def __init__(self, degrees):
        self.degrees = degrees

    def sin_solution(self):
        sin_value = math.sin(self.degrees)
        return sin_value

    def cos_solution(self):
        cos_value = math.cos(self.degrees)
        return cos_value

    def tan_solution(self):
        tan_value = math.tan(self.degrees)
        return tan_value
