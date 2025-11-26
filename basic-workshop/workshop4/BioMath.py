class Person:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
    def cal_bmi(self):
        return self.weight / (self.height ** 2)