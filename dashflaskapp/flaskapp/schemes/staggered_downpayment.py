class StaggeredDownpayment():
    def __init__(self, inputs):
        self.applied = inputs.appliedForFlat.data
        self.relationship = inputs.relationship.data
        self.loan = inputs.loan.data
        self.lease = inputs.remainingLease.data

    def checkEligibility(self):
        name = "Staggered Downpayment Scheme\n"
        footnote = \
	'''
            Amount payable during collection of keys is dependent on date when new flat is booked
            More info <a href="https://www.hdb.gov.sg/residential/buying-a-flat/new/schemes-and-grants/staggered-downpayment-scheme" class="alert-link">here</a>
	''' 
        try:
            assert self.applied == 'Yes'
        except AssertionError:
            return 'Not eligible for Staggered Downpayment Scheme'

        if self.loan == 'No loan' or self.loan == 'HDB Housing loan':
            bracket = '''
            1) Downpayment at signing of lease: 5% using CPF or cash
            2) Payment during key collection: 5% using CPF or cash\n
            '''
        elif self.loan == 'Bank loan':
            bracket = '''
            For new flats booked before 6 July 2018:
            1) Downpayment at signing of lease: 5% minimum cash payment and 5% using CPF or cash (Loan ceiling of 80%) OR 10% minimum cash payment (loan ceiling of 60%)\n
            2) Payment during key collection: 10% using CPF or cash (Loan ceiling of 80%) OR 30% using CPF or cash (Loan ceiling of 60%)

            For new flats booked on or after 6 July 2018:
            1) Downpayment at signing of lease: 5% minimum cash payment and 5% using CPF or cash (Loan ceiling of 75%) OR 10% minimum cash payment (loan ceiling of 55%)\n
            2) Payment during key collection: 15% using CPF or cash (Loan ceiling of 75%) OR 35% using CPF or cash (Loan ceiling of 55%)\n
            '''
        
        if self.relationship != 'First Timer Couple' or self.relationship != 'First Timer with Second Timer Spouse':
            if self.lease > 0:
                return name + bracket + footnote
            else:
                return "Not eligible for Staggered Downpayment Scheme"
        else:
            return name + bracket + footnote
        