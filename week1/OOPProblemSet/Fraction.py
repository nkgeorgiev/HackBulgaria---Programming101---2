class Fraction:
    def __init__(self, num=1, denum=1):
        self.num = num
        self.denum = denum

    def __eq__(self, other):
        return self.num * other.denum == self.denum * other.num

    def __add__(self, other):
        num = self.num * other.denum + other.num * self.denum
        denum = self.denum * other.denum
        return Fraction(num, denum)

    def __sub__(self, other):
        num = self.num * other.denum - other.num * self.denum
        denum = self.denum * other.denum
        return Fraction(num, denum)

    def __lt__(self, other):
        return self.num * other.denum < self.denum * other.num

    def __gt__(self, other):
        return self.num * other.denum < self.denum * other.num
