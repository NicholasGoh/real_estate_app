class HousingGrantsForHDB:
    def __init__(self, inputs):
        self.avgIncome = inputs.avgIncome.data
        # self.age = inputs.age.data
        # self.noOfRooms = inputs.noOfRoom.data
        self.firstTime = inputs.firstTime.data
        self.relationship = inputs.relationship.data
        self.employment = inputs.employment.data
        self.remainingLease = inputs.remainingLease.data
    def checkEligibility(self):
        name = 'Housing Grant for HDB'
        footnote = \
	'''
        You and the other flat applicants must not own any of the following properties whether locally or overseas, or have disposed of any such properties in the 30 months before your new flat application:
        1) Private residential property (including privatised HUDC flats and ECs)
        2) House
        3) Building
        4) Land
        More info <a href="https://www.hdb.gov.sg/residential/buying-a-flat/new/schemes-and-grants/cpf-housing-grants-for-hdb-flats" class="alert-link">here</a>
	'''
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
        grant = 8 * 10 ** 4
        while grant > 0 and avgIncome > 1500:
            grant -= 5000
            avgIncome -= 500
        # grant = additional cpf housing grant + special cpf housing grant
        # grant = ahg + shg
        if grant < 45000:
            ahg = 0
            shg = grant
        else:
            ahg = grant - 4 * 10 ** 4
            shg = grant - ahg
        return [name, True, f'Additional CPF housing grant: {ahg}\n Special CPF housing grant: {shg} ' + footnote]
