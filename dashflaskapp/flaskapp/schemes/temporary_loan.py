class TemporaryLoan():
    def __init__(self, inputs):
        self.applied = inputs.appliedForFlat.data
    
    def checkEligibility(self):
        name = "Temporary Loan Scheme\n"
        footnote = \
	'''
        You must have sufficient cash/CPF from sale of existing flat to fully repay the temporary loan.
        More info <a href="https://www.hdb.gov.sg/residential/buying-a-flat/new/schemes-and-grants/temporary-loan-scheme">here</a>
	'''

        try:
            assert self.applied == True
        except AssertionError:
            return 'Not eligible for Temporary Loan Scheme'

        return name + "Eligible for Temporary Loan Scheme" + footnote