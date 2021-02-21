class HousingGrantsForEC():
    def __init__(self, inputs):
        self.age = inputs.age
        pass
    def returnBracket(self):
        if 30 < self.age.data < 40:
            return 1000
        else:
            return 2000
