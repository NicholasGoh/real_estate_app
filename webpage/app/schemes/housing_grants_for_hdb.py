class HousingGrantsForHDB:
    def __init__(self, inputs):
        self.avgIncome = inputs.avgIncome 
        self.firstTime = inputs.firstTime 
        self.relationship = inputs.relationship 
        self.employment = inputs.employment 
        self.remainingLease = inputs.remainingLease 
    def firstTime_brackets(self):
        footnote = \
	'''
	   You and the other flat applicants must not:\
	   Own any of the following properties whether locally or overseas,
	   or have disposed of any such properties in the 30 months before your new flat application:
	   Private residential property (including privatised HUDC flats and ECs)
	   House
	   Building
	   Land
	'''
        try:
            # assert all_applicants are fulltimers
            assert avgIncome <= 9000
            assert firstTime == True
            # work continuously for 12 months prior to application
            # still working at submission of application
            assert employment == True
            assert remainingLease >= 20
        except AssertionError:
            return 0, 0, footnote

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
        return ahg, shg, footnote
