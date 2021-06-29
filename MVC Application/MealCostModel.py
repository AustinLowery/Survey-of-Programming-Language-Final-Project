
class Model:
    def __init__(self, cost=None, tip=None, tax=None):
        self.cost = cost
        self.tip = tip
        self.tax = tax

    def compute_total(self):
        return round(self.cost * (1+self.tax) + self.tip, 2)


if __name__ == "__main__":
    print("Please run the Meal Cost Controller.")
