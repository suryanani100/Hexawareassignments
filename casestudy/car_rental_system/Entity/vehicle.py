class Vehicle:
    def __init__(self, vehicle_id, make, model, year, daily_rate, status, passenger_capacity, engine_capacity):
        self._vehicle_id = vehicle_id
        self._make = make
        self._model = model
        self._year = year
        self._daily_rate = daily_rate
        self._status = status
        self._passenger_capacity = passenger_capacity
        self._engine_capacity = engine_capacity

    @property
    def vehicle_id(self):
        return self._vehicle_id

    @property
    def make(self):
        return self._make

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year

    @property
    def daily_rate(self):
        return self._daily_rate

    @property
    def status(self):
        return self._status

    @property
    def passenger_capacity(self):
        return self._passenger_capacity

    @property
    def engine_capacity(self):
        return self._engine_capacity

    @vehicle_id.setter
    def vehicle_id(self, value):
        self._vehicle_id = value

    @make.setter
    def make(self, value):
        self._make = value

    @model.setter
    def model(self, value):
        self._model = value

    @year.setter
    def year(self, value):
        self._year = value

    @daily_rate.setter
    def daily_rate(self, value):
        self._daily_rate = value

    @status.setter
    def status(self, value):
        self._status = value

    @passenger_capacity.setter
    def passenger_capacity(self, value):
        self._passenger_capacity = value

    @engine_capacity.setter
    def engine_capacity(self, value):
        self._engine_capacity = value
