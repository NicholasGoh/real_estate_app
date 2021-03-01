class HousingGrantsForEC:
    def __init__(self, inputs):
        self.avgIncome = inputs.avgIncome.data
        # self.age = inputs.age.data
        # self.noOfRooms = inputs.noOfRoom.data
        self.firstTime = inputs.firstTime.data
        self.relationship = inputs.relationship.data
        self.employment = inputs.employment.data
        self.remainingLease = inputs.remainingLease.data
    def firstTime_bracket(self):
        name = 'Housing Grant for EC\n'
        footnote = \
	'''
           More info <a href="https://www.hdb.gov.sg/residential/buying-a-flat/new/schemes-and-grants/cpf-housing-grants-for-ecs" class="alert-link">here</a>
	'''
        # Enhanced CPF Housing Grant EHG
        try:
            # assert all_applicants are fulltimers
            assert self.firstTime == 'Yes'
        except AssertionError:
            return name + 'grant given: 0 ' + footnote

        grant = 0
        if self.relationship == 'First Timer Couple' or self.relationship == 'First Timer with Singapore Permanent Resident Spouse':
            avgIncome = self.avgIncome
            grant = 3 * 10 ** 4
            while grant > 0 and avgIncome > 10 ** 4:
                grant -= 10 ** 4
                avgIncome -= 1000
            if self.relationship == 'First Timer with Singapore Permanent Resident Spouse':
                grant = grant if grant == 0 else grant - 10 ** 4
        elif self.relationship == 'First Timer with Second Timer Spouse':
            avgIncome = self.avgIncome
            grant = 15000
            while grant > 0 and avgIncome > 10 ** 4:
                grant -= 5000
                avgIncome -= 1000
        return name + f'grant given: {grant} ' + footnote
