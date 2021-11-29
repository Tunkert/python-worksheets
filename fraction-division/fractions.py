class Fraction:
    def __init__(self, numerator_1, numerator_2, denominator_1, denominator_2):
        self.numerator_1 = numerator_1
        self.numerator_2 = numerator_2
        self.denominator_1 = denominator_1
        self.denominator_2 = denominator_2

    def numerator_product(self):
        num_prod = self.numerator_1 * self.denominator_2
        return num_prod

    def denominator_product(self):
        den_prod = self.denominator_1 * self.numerator_2
        return den_prod

    def find_gcf(self):
        gcf = 1
        if self.numerator_product() >= self.denominator_product():
            for x in range(2, self.denominator_product()):
                if self.numerator_product() % x == 0 and self.denominator_product() % x == 0:
                    gcf = x
        if self.numerator_product() <= self.denominator_product():
            for x in range(2, self.numerator_product()):
                if self.numerator_product() % x == 0 and self.denominator_product() % x == 0:
                    gcf = x
        return gcf

    def reduced_numerator(self):
        red_num = self.numerator_product() / self.find_gcf()
        return red_num

    def reduced_denominator(self):
        red_den = self.denominator_product() / self.find_gcf()
        return red_den 
