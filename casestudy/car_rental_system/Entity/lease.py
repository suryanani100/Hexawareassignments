class Lease:
    def __init__(self, lease_id, vehicle_id, customer_id, start_date, end_date, category):
        self._lease_id = lease_id
        self._vehicle_id = vehicle_id
        self._customer_id = customer_id
        self._start_date = start_date
        self._end_date = end_date
        self._category = category

    @property
    def lease_id(self):
        return self._lease_id

    @property
    def vehicle_id(self):
        return self._vehicle_id

    @property
    def customer_id(self):
        return self._customer_id

    @property
    def start_date(self):
        return self._start_date

    @property
    def end_date(self):
        return self._end_date

    @property
    def category(self):
        return self._category

    @lease_id.setter
    def lease_id(self, value):
        self._lease_id = value

    @vehicle_id.setter
    def vehicle_id(self, value):
        self._vehicle_id = value

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value

    @start_date.setter
    def start_date(self, value):
        self._start_date = value

    @end_date.setter
    def end_date(self, value):
        self._end_date = value

    @category.setter
    def category(self, value):
        self._category = value
