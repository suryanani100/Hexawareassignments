class Customer:
    def __init__(self, customer_id, firstname, lastname, email, phone_number):
        self._customer_id = customer_id
        self._firstname = firstname
        self._lastname = lastname
        self._email = email
        self._phone_number = phone_number

    @property
    def customer_id(self):
        return self._customer_id

    @property
    def first_name(self):
        return self._firstname

    @property
    def last_name(self):
        return self._lastname

    @property
    def email(self):
        return self._email

    @property
    def phone_number(self):
        return self._phone_number

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value

    @first_name.setter
    def first_name(self, value):
        self._firstname = value

    @last_name.setter
    def last_name(self, value):
        self._lastname = value

    @email.setter
    def email(self, value):
        self._email = value

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value
