from app.schemes.housing_grants_for_ec import HousingGrantsForEC

class SchemeManager():
    def __init__(self, inputs):
        self.scheme1Output = HousingGrantsForEC(inputs).returnBracket()
    def foo(self):
        return [self.scheme1Output]
