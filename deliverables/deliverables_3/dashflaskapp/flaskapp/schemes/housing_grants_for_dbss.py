class HousingGrantsForDBSS:
    def __init__(self, inputs):
        self.avgIncome = inputs.avgIncome.data
        # self.age = inputs.age.data
        # self.noOfRooms = inputs.noOfRoom.data
        self.firstTime = inputs.firstTime.data
        self.relationship = inputs.relationship.data
        self.employment = inputs.employment.data
        self.remainingLease = inputs.remainingLease.data
    def checkEligibility(self):
        name = 'Housing Grant for DBSS'
        footnote = \
	'''
           More info <a href="https://www.hdb.gov.sg/residential/buying-a-flat/new/schemes-and-grants/cpf-housing-grants-for-dbss-flats" class="alert-link">here</a>
	'''
        # Enhanced CPF Housing Grant EHG
        try:
            # assert all_applicants are fulltimers
            assert self.firstTime == 'Yes'
            # work continuously for 12 months prior to application
            # still working at submission of application
            assert self.employment == 'Yes'
            assert self.remainingLease >= 20
        except AssertionError:
            return [name, False, footnote]

        avgIncome = self.avgIncome
        grant = 0
        if self.relationship == 'First Timer Couple':
            grant = 8 * 10 ** 4
            while grant > 0 and avgIncome > 1500:
                grant -= 5000
                avgIncome -= 500
        elif self.relationship == 'Single First Timer':
            grant = 4 * 10 ** 4
            while grant > 0 and avgIncome > 750:
                grant -= 2500
                avgIncome -= 250
        return [name, True, f'Enhanced CPF Housing Grant given: {grant} ' + footnote]
