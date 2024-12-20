"""MODULE: order_request. Contains the order request class"""

import hashlib
import json
from datetime import datetime
from .atributo_product_id import ProductId
from .atributo_order_type import OrderType
from .atributo_address import Address
from .atributo_phone_number import PhoneNumber
from .atributo_zip_code import ZipCode

class OrderRequest:
    """Class representing the register of the order in the system"""
    #pylint: disable=too-many-arguments
    def __init__( self, product_id, order_type,
                  delivery_address, phone_number, zip_code ):
        self.__product_id = ProductId(product_id).validate_attr(product_id)
        self.__delivery_address = Address(delivery_address).validate_attr(delivery_address)
        self.__order_type = OrderType(order_type).validate_attr(order_type)
        self.__phone_number = PhoneNumber(phone_number).validate_attr(phone_number)
        self.__zip_code = ZipCode(zip_code).validate_attr(zip_code)
        justnow = datetime.utcnow()
        self.__time_stamp = datetime.timestamp(justnow)
        self.__order_id =  hashlib.md5(self.__str__().encode()).hexdigest()

    def __str__(self):
        return "OrderRequest:" + json.dumps(self.__dict__)

    @property
    def delivery_address( self ):
        """Property representing the address where the product
        must be delivered"""
        return self.__delivery_address

    @delivery_address.setter
    def delivery_address( self, value ):
        self.__delivery_address = value

    @property
    def order_type( self ):
        """Property representing the type of order: REGULAR or PREMIUM"""
        return self.__order_type
    @order_type.setter
    def order_type( self, value ):
        self.__order_type = value

    @property
    def phone_number( self ):
        """Property representing the clients's phone number"""
        return self.__phone_number
    @phone_number.setter
    def phone_number( self, value ):
        self.__phone_number = value

    @property
    def product_id( self ):
        """Property representing the products  EAN13 code"""
        return self.__product_id
    @product_id.setter
    def product_id( self, value ):
        self.__product_id = value

    @property
    def time_stamp(self):
        """Read-only property that returns the timestamp of the request"""
        return self.__time_stamp

    @property
    def order_id( self ):
        """Returns the md5 signature"""
        return self.__order_id

    @property
    def zip_code( self ):
        """Returns the order's zip_code"""
        return self.__zip_code
