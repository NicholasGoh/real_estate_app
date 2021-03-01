class DeferredDownpayment:
    def __init__(self, inputs):
        self.age = inputs.age.data
        self.applied = inputs.appliedForFlat.data

    def checkEligibility(self):
        name = 'Deferred Downpayment Scheme:\n'
        footnote = \
	'''
        You must have not sold or completed the sale of your existing flat at the point of new flat application
        More info <a href="https://www.hdb.gov.sg/residential/buying-a-flat/new/schemes-and-grants/deferred-downpayment-scheme" class="alert-link">here</a>
	'''

        try:
            assert self.applied == 'Yes'
            assert self.age >= 55
        except AssertionError:
            return 'Not eligible for Deferred Downpayment Scheme'

        return name + "Eligible for Deferred Downpayment Scheme" + footnote