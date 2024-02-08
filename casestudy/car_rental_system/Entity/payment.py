class Payment:
    def __init__(self, payment_id, lease_id, payment_date, amount):
        self._payment_id = payment_id
        self._lease_id = lease_id
        self._payment_date = payment_date
        self._amount = amount

    @property
    def payment_id(self):
        return self._payment_id

    @property
    def lease_id(self):
        return self._lease_id

    @property
    def payment_date(self):
        return self._payment_date

    @property
    def amount(self):
        return self._amount

    @payment_id.setter
    def payment_id(self, value):
        self._payment_id = value

    @lease_id.setter
    def lease_id(self, value):
        self._lease_id = value

    @payment_date.setter
    def payment_date(self, value):
        self._payment_date = value

    @amount.setter
    def amount(self, value):
        self._amount = value
