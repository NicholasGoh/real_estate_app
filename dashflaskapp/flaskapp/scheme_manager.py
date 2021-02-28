from flaskapp.schemes.housing_grants_for_hdb import HousingGrantsForHDB
from flaskapp.schemes.housing_grants_for_dbss import HousingGrantsForDBSS
from flaskapp.schemes.housing_grants_for_ec import HousingGrantsForEC

class SchemeManager():
    def __init__(self, inputs):
        self.scheme1Output = HousingGrantsForHDB(inputs).firstTime_bracket()
        self.scheme2Output = HousingGrantsForDBSS(inputs).firstTime_bracket()
        self.scheme3Output = HousingGrantsForEC(inputs).firstTime_bracket()
    def foo(self):
        return [self.scheme1Output, self.scheme2Output, self.scheme3Output]
