import operator

class Bag:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

bag1 = Bag(["Book", "Pen"])
bag2 = Bag([])

print(operator.truth(bag1))
print(operator.truth(bag2))

class Bag:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

bag1 = Bag(["Book", "Pen"])
bag2 = Bag([])

print(operator.truth(bag1))
print(operator.truth(bag2))