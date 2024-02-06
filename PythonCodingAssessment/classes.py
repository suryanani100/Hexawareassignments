class Product:
    def __init(self,product_id,product_name,description,price,qtyinstock,product_type):
        self._product_id = product_id
        self._product_name = product_name
        self._description = description
        self._price = price
        self._qtyinstock = qtyinstock
        self._product_type = product_type

    @property
    def product_id(self):
        return self._product_id

    @property
    def product_name(self):
        return self._product_name

    @property
    def description(self):
        return self._description

    @property
    def price(self):
        return self._price

    @property
    def qtyinstock(self):
        return self._qtyinstock

    @property
    def product_type(self):
        return self._product_type

    @product_id.setter
    def product_id(self,pro_id):
        self.product_id = pro_id

    @product_name.setter
    def product_name(self,name):
        self.product_name = name

    @description.setter
    def description(self,desc):
        self.description = desc

    @price.setter
    def price(self,rate):
        self.price = rate

    @qtyinstock.setter
    def qtyinstock(self,quantity):
        self.qtyinstock = quantity

    @product_type.setter
    def product_type(self,pro_type):
        self.product_type=pro_type


class Electronics:
    def __init__(self,product_id,product_name,description,price,qtyinstock,product_type, brand, warranty_period):
        super().__init__(product_id,product_name,description,price,qtyinstock,product_type)
        self._brand = brand
        self._warranty_period = warranty_period

    @property
    def brand(self):
        return self._brand

    @property
    def warranty_period(self):
        return self._warranty_period

    @brand.setter
    def brand(self, value):
        self._brand = value

    @warranty_period.setter
    def warranty_period(self,warranty):
        self.warranty_period = warranty


class Clothing(Product):
    def __init__(self,product_id,product_name,description,price,qtyinstock,product_type,size,colour):
        super().__init__(product_id,product_name,description,price,qtyinstock,product_type)
        self._size=size
        self._colour=colour

    @property
    def size(self):
        return self._size

    @property
    def colour(self):
        return self._colour

    @size.setter
    def size(self,size):
        self.size = size

    @colour.setter
    def colour(self,color):
        self.colour = color


class user:
    def __init__(self,user_id,user_name,password,role):
        self._user_id = user_id
        self._user_name = user_name
        self._password = password
        self._role = role

    @property
    def user_id(self):
        return self._user_id

    @property
    def username(self):
        return self._user_name

    @property
    def password(self):
        return self._password

    @property
    def role(self):
        return self._role

    @username.setter
    def username(self,value):
        self.user_name = value

    @password.setter
    def password(self,val):
        self.password=val

    @role.setter
    def role(self,val):
        self.role=val
