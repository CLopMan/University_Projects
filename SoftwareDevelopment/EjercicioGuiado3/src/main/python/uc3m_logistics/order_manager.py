"""Module """
import re
import os
import json
from datetime import datetime
from .order_shipping import OrderShipping
from .order_request import OrderRequest
from .order_management_exception import OrderManagementException



class OrderManager:
    """Class for providing the methods for managing the orders"""

    def init(self):
        """init"""
        # pylint: disable-next=unnecessary-pass
        pass

    @staticmethod
    def validate_ean13(ean13):
        """Receives a barcode and validates it checking the
        control digit.
        Algorithm:
        https://es.wikipedia.org/wiki/European_Article_Number#Estructura_y_partes
        :param eAn13: barcode
        :return: boolean
        """

        if not re.fullmatch('^[0-9]{13}$', ean13):
            return False
        sum_odd = 0
        sum_even = 0

        for i in range(len(ean13) - 1):
            # not equal to correct the index starting.
            # Should start in 1.
            sumando = int(ean13[i])
            if i % 2 != 0:
                sum_even += sumando
            else:
                sum_odd += sumando
        sum_even *= 3
        validation = (10 - ((sum_odd + sum_even) % 10)) % 10
        if int(ean13[-1]) != validation:
            return False

        return True

    @staticmethod
    def validate_address(address):
        """method that validate the address"""
        if len(address) < 20 or len(address) > 100:
            return False
        cont_sp = 0

        for i in range(len(address)):
            if address[i] == ' ':
                cont_sp += 1

        if cont_sp < 1:
            return False
        return True

    @property
    def store_path(self):
        """Return the relative path"""
        # Path
        path = os.path.dirname(__file__)
        path = path[:-26]
        return os.path.join(path, "json")

    def register_order(self, product_id, order_type, address, phone_number, zip_code):
        """Method 1"""
        # INPUT VALIDATION
        if not isinstance(product_id, str):

            raise OrderManagementException\
                ("Exception: Product Id type not valid")

        if not self.validate_ean13(product_id):
            raise OrderManagementException\
                ("Exception: Product Id not valid")

        if not isinstance(order_type, str):
            raise OrderManagementException\
                ("Exception: orderType type not valid")

        if order_type.upper() != "REGULAR" and order_type.upper() != "PREMIUM":
            raise OrderManagementException\
                ("Exception: orderType not valid")

        if not isinstance(address, str):
            raise OrderManagementException\
                ("Exception : address type not valid")

        if not self.validate_address(address):
            raise OrderManagementException\
                ("Exception : address not valid")

        if not isinstance(phone_number, str):
            raise OrderManagementException\
                ("Exception : phone_number type not valid")

        if len(phone_number) != 9:
            raise OrderManagementException\
                ("Exception : phone_number not valid")

        try:
            int(phone_number)
        except:
            raise OrderManagementException\
                ("Exception : phone_number not valid")

        if not isinstance(zip_code, str):
            raise OrderManagementException\
                ("Exception : zipcode type not valid")
        if len(zip_code) != 5:
            raise OrderManagementException\
                ("Exception : zipcode not valid")
        try:
            aux_zip_code = int(zip_code)
            if not 1000 <= aux_zip_code < 53000:
                raise OrderManagementException\
                    ("Exception : zipcode doesn't exists")
        except:
            raise OrderManagementException\
                ("Exception : zipcode not valid")

        # GENERATES REQUEST
        ord_requ = OrderRequest(product_id, order_type, address, phone_number, zip_code)
        out = ord_requ.order_id

        # OPENS THE STORE_FILE. IF NOT EXISTS CREATES IT
        try:
            with open(self.store_path + "/Almacen.JSON", "r", encoding="utf-8") as file:
                data_list = json.load(file)
        except FileNotFoundError:
            data_list = []

        ## adds the hash to the file
        data_list.append(ord_requ.__dict__)
        data_list[-1]["_OrderRequest__order_id"] = out

        # WRITES EVERYTTHING ON STORE_FILE
        with open(self.store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
            json.dump(data_list, file, indent=2)

        # returns hash
        return out

    def send_code(self, input_file):
        """Method 2"""
        file_store = self.store_path + "/Almacen.JSON"
        if not os.path.isfile(file_store):
            raise OrderManagementException("There isn't any store")
        try:
            with open(file_store, "r", encoding="utf8") as file:
                data_list = json.load(file)
        except FileNotFoundError as ex:
            raise OrderManagementException\
                ("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise OrderManagementException\
                ("JSON Decode Error - Wrong JSON Format") from ex

        try:
            with open(input_file, "r", encoding="utf8") as file:
                dicc_json = json.load(file)
        except FileNotFoundError as ex:
            raise OrderManagementException\
                ("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise OrderManagementException\
                ("JSON Decode Error - Wrong JSON Format") from ex

        claves = tuple(dicc_json.keys())

        if len(claves) != 2:
            raise OrderManagementException\
                ("There are too/few keys")
        if tuple(claves)[0] != "OrderID":
            raise OrderManagementException\
                ("Incorrect keys")
        if tuple(dicc_json.keys())[1] != "ContactEmail":
            raise OrderManagementException\
                ("Incorrect keys")
        if not re.fullmatch('^[0-9|a-f]{32}$', dicc_json["OrderID"]):
            raise OrderManagementException\
                ("Wrong Hash")
        if not re.fullmatch('^[0-9|a-z][0-9|a-z]*[@][0-9|a-z][0-9|a-z]*'
                            '[.][0-9|a-z][0-9|a-z]*$', dicc_json["ContactEmail"]):
            raise OrderManagementException\
                ("Wrong Contact Email")

        try:
            for item in data_list:
                if item["_OrderRequest__order_id"] == dicc_json["OrderID"]:
                    product_id = item["_OrderRequest__product_id"]
                    order_id = item["_OrderRequest__order_id"]
                    delivery_email = dicc_json["ContactEmail"]
                    order_type = item["_OrderRequest__order_type"]
                    ord_shi = OrderShipping\
                        (product_id, order_id, delivery_email, order_type)
                    out = ord_shi.tracking_code
                    with open(self.store_path + "/Almacen.JSON", "w",
                              encoding="utf-8", newline="") as file:
                        json.dump(data_list, file, indent=2)
                    req = OrderRequest(product_id, order_type,
                                                     item["_OrderRequest__delivery_address"],
                                                     item["_OrderRequest__phone_number"],
                                                     item["_OrderRequest__zip_code"])
                    req.time_stamp = item["_OrderRequest__time_stamp"]
                    real_hash = req.order_id

                    if real_hash != dicc_json["OrderID"]:
                        raise OrderManagementException\
                            ("The hash has been manipulated")

                    dicc_salida = ord_shi.__dict__

                    try:
                        with open(self.store_path + "/Almacenf2.JSON", "r",
                                  encoding="utf-8") as file:
                            salida_list = json.load(file)
                    except FileNotFoundError:
                        salida_list = []

                    salida_list.append(dicc_salida)

                    with open(self.store_path + "/Almacenf2.JSON", "w",
                              encoding="utf-8", newline="") as file:
                        json.dump(salida_list, file, indent=2)
                    return out
        except:
            raise OrderManagementException\
                ("Your OrderId doesn't exist")
    def send_product(self,tracking_number):
        """Method 3"""
        file_store = self.store_path + "/Almacenf2.JSON"
        if not os.path.isfile(file_store):
            raise OrderManagementException\
                ("There isn't any store")
        if not re.fullmatch('^[0-9|a-f]{64}$', tracking_number):
            raise OrderManagementException\
                ("Wrong Hash")
        try:
            with open(file_store, "r", encoding="utf8") as file:
                data_list = json.load(file)
        except json.JSONDecodeError as ex:
            raise OrderManagementException\
                ("JSON Decode Error - Wrong JSON Format") from ex

        for item in data_list:
            if item["_OrderShipping__tracking_code"] == tracking_number:
                if item["_OrderShipping__delivery_day"] != \
                        datetime.timestamp(datetime.utcnow()):
                    raise OrderManagementException\
                        ("The delivery day isn't today")

                dicc_salida = {}
                dicc_salida["Delivery_day_"] = item["_OrderShipping__delivery_day"]
                dicc_salida["Tracking_code_"] = tracking_number

                try:
                    with open(self.store_path + "/Almacenf3.JSON", "r", encoding="utf-8") as file:
                        salida_list = json.load(file)
                except FileNotFoundError:
                    salida_list = []
                salida_list.append(dicc_salida)

                with open(self.store_path + "/Almacenf3.JSON", "w",
                          encoding="utf-8", newline="") as file:
                    json.dump(data_list, file, indent=2)

                return True
        return False
