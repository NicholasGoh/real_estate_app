from flaskapp.schemes.housing_grants_for_hdb import HousingGrantsForHDB
from flaskapp.schemes.housing_grants_for_dbss import HousingGrantsForDBSS
from flaskapp.schemes.housing_grants_for_ec import HousingGrantsForEC
from flaskapp.schemes.staggered_downpayment import StaggeredDownpayment
from flaskapp.schemes.deferred_downpayment import DeferredDownpayment
from flaskapp.schemes.temporary_loan import TemporaryLoan
from flaskapp.schemes.fresh_start_housing import FreshStartHousing

class SchemeManager():
    def __init__(self, inputs):
        self.scheme1Output = HousingGrantsForHDB(inputs).firstTime_bracket()
        self.scheme2Output = HousingGrantsForDBSS(inputs).firstTime_bracket()
        self.scheme3Output = HousingGrantsForEC(inputs).firstTime_bracket()
        self.scheme4Output = StaggeredDownpayment(inputs).checkEligibility()
        self.scheme5Output = DeferredDownpayment(inputs).checkEligibility()
        self.scheme6Output = TemporaryLoan(inputs).checkEligibility()
        self.scheme7Output = FreshStartHousing(inputs).checkEligibility()
    def foo(self):
        return [self.scheme1Output, self.scheme2Output, self.scheme3Output,  self.scheme4Output, self.scheme5Output, self.scheme6Output, self.scheme7Output]
