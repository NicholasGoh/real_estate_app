class FreshStartHousing():
    def __init__(self, inputs):
        self.relationship = inputs.relationship.data
        self.age = inputs.age.data
        self.employment = inputs.employment.data
        self.avgIncome = inputs.avgIncome.data
    
    def checkEligibility(self):
        name = "Fresh Start Housing Scheme"
        footnote = \
	'''
        You must have occupoed a public rental flat for at least 1 year and not own any other properties overseas or locally
        More info <a href="https://www.hdb.gov.sg/residential/buying-a-flat/new/schemes-and-grants/temporary-loan-scheme" class="alert-link>here</a>
	'''
        try:
            assert self.employment == 'Yes'
            assert self.avgIncome < 7000
            assert self.employment == 'Yes'
            assert self.relationship == "Second Timer Couple"
            assert self.age < 55
            assert self.age >= 35
        except AssertionError:
            return [name, False, footnote]

        return [name, True, footnote]