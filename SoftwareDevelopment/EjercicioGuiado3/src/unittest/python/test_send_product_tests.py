"""class for testing the regsiter_order method"""
import json
import unittest
import os
from freezegun import freeze_time
from uc3m_logistics import order_manager, order_management_exception

store_path = os.path.dirname(__file__)[:-15] + "json"


@freeze_time("01-01-2000")
class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""
    def setUp(self) -> None:
        a = order_manager.OrderManager()
        file_store = a.store_path + "/Almacenf2.JSON"
        if os.path.isfile(file_store):
            os.remove(file_store)

    def test_f3_Vt1(self):
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderShipping__alg": "SHA-256",
                    "_OrderShipping__type": "DS",
                    "_OrderShipping__product_id": "8421691423220",
                    "_OrderShipping__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4",
                    "_OrderShipping__delivery_email": "adrian@gmail.com",
                    "_OrderShipping__issued_at": -2208974400.0,
                    "_OrderShipping__delivery_day": 946684800.0,
                    "_OrderShipping__tracking_code": "5856fbd8f18ad8381d45e0efe946025037a3dfe689f285c1dab0b48ef91df0f0"}
        dicc_json.append(order_ex)
        with open(store_path + "/Almacenf2.JSON", "w", encoding="utf-8", newline="") as file:
            json.dump(dicc_json, file, indent=2)

        a = order_manager.OrderManager()
        file_store = a.store_path + "/Almacenf3.JSON"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_order = order_manager.OrderManager()
        value = my_order.send_product("5856fbd8f18ad8381d45e0efe946025037a3dfe689f285c1dab0b48ef91df0f0")
        found = False
        # Comprobamos que haya creado el almacen
        if os.path.isfile(file_store):
            found = True
        self.assertTrue(found)
        self.assertEqual(True,value)

    def test_f3_Vt2(self):
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderShipping__alg": "SHA-256",
                    "_OrderShipping__type": "DS",
                    "_OrderShipping__product_id": "8421691423220",
                    "_OrderShipping__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4",
                    "_OrderShipping__delivery_email": "adrian@gmail.com",
                    "_OrderShipping__issued_at": -2208974400.0,
                    "_OrderShipping__delivery_day": 946684800.0,
                    "_OrderShipping__tracking_code": "5856fbd8f18ad8381d45e0efe946025037a3dfe689f285c1dab0b48ef91df0f0"}
        dicc_json.append(order_ex)

        with open(store_path + "/Almacenf2.JSON", "w", encoding="utf-8", newline="") as file:
            json.dump(dicc_json, file, indent=2)

        my_order = order_manager.OrderManager()
        value = my_order.send_product("5856fbd8f18ad8381d45e0efe946025037a3dfe689f285c1dab0b48ef91df0f0")
        self.assertEqual(True,value)

    def test_f3_NVt1(self):
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderShipping__alg": "SHA-256",
                    "_OrderShipping__type": "DS",
                    "_OrderShipping__product_id": "8421691423220",
                    "_OrderShipping__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4",
                    "_OrderShipping__delivery_email": "adrian@gmail.com",
                    "_OrderShipping__issued_at": -2208974400.0,
                    "_OrderShipping__delivery_day": -2208888000.0,
                    "_OrderShipping__tracking_code": "5856fbd8f18ad8381d45e0efe946025037a3dfe689f285c1dab0b48ef91df0f0"}
        dicc_json.append(order_ex)
        with open(store_path + "/Almacenf2.JSON", "w", encoding="utf-8", newline="") as file:
            json.dump(dicc_json, file, indent=2)

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_product("0")
        self.assertEqual("Wrong Hash", cm.exception.message)

    def test_f3_NVt2(self):
        # Orden de ejemplo en el almacen


        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_product("5856fbd8f18ad8381d45e0efe946025037a3dfe689f285c1dab0b48ef91df0f0")
        self.assertEqual("There isn't any store", cm.exception.message)



    def test_f3_NVt3(self):
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderShipping__alg": "SHA-256",
                    "_OrderShipping__type": "DS",
                    "_OrderShipping__product_id": "8421691423220",
                    "_OrderShipping__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4",
                    "_OrderShipping__delivery_email": "adrian@gmail.com",
                    "_OrderShipping__issued_at": -2208974400.0,
                    "_OrderShipping__delivery_day": -2208888000.0,
                    "_OrderShipping__tracking_code": "5856fbd8f18ad8381d45e0efe946025037a3dfe689f285c1dab0b48ef91df0f0"}
        dicc_json.append(order_ex)
        with open(store_path + "/Almacenf2.JSON", "w", encoding="utf-8", newline="") as file:
             json.dump(dicc_json, file, indent=2)
        my_order = order_manager.OrderManager()
        value = my_order.send_product("5856fbd8f18ad8381d45e0efe946025037a3dfe689f285c1dab0b48ef91df0f1")
        self.assertEqual(False, value)

    def test_f3_NVt4(self):
        # escribe algo que no sea un
        with open(store_path + "/Almacenf2.JSON", "w", encoding="utf-8", newline="") as file:
            file.write("esto va a dar tremendo decode-error")

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_product("5856fbd8f18ad8381d45e0efe946025037a3dfe689f285c1dab0b48ef91df0f0")
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)


    def test_f3_NVt5(self):
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderShipping__alg": "SHA-256",
                    "_OrderShipping__type": "DS",
                    "_OrderShipping__product_id": "8421691423220",
                    "_OrderShipping__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4",
                    "_OrderShipping__delivery_email": "adrian@gmail.com",
                    "_OrderShipping__issued_at": -2208974400.0,
                    "_OrderShipping__delivery_day": -2208888000.0,
                    "_OrderShipping__tracking_code": "5856fbd8f18ad8381d45e0efe946025037a3dfe689f285c1dab0b48ef91df0f0"}
        dicc_json.append(order_ex)
        with open(store_path + "/Almacenf2.JSON", "w", encoding="utf-8", newline="") as file:
            json.dump(dicc_json, file, indent=2)

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_product("5856fbd8f18ad8381d45e0efe946025037a3dfe689f285c1dab0b48ef91df0f0")
        self.assertEqual("The delivery day isn't today", cm.exception.message)

    def test_f3_vt5(self):
        """bucle 2 veces"""
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex1 = {"_OrderShipping__alg": "SHA-256",
                    "_OrderShipping__type": "DS",
                    "_OrderShipping__product_id": "8421691423220",
                    "_OrderShipping__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4",
                    "_OrderShipping__delivery_email": "adrian@gmail.com",
                    "_OrderShipping__issued_at": -2208974400.0,
                    "_OrderShipping__delivery_day": -2208888000.0,
                    "_OrderShipping__tracking_code": "5856fbd8f18ad8381d45e0efe946025037a3dfe689f285c1dab0b48ef91df0f0"}
        dicc_json.append(order_ex1)

        order_ex2 ={"_OrderShipping__alg": "SHA-256",
                    "_OrderShipping__type": "DS",
                    "_OrderShipping__product_id": "8421691423220",
                    "_OrderShipping__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4",
                    "_OrderShipping__delivery_email": "adrian@gmail.com",
                    "_OrderShipping__issued_at": -2208974400.0,
                    "_OrderShipping__delivery_day": -2208888000.0,
                    "_OrderShipping__tracking_code": "5856fbd8f18ad8381d45e0efe946025037a3dfe689f285c1dab0b48ef91df0f0"}
        dicc_json.append(order_ex2)

        with open(store_path + "/Almacenf2.JSON", "w", encoding="utf-8", newline="") as file:
            json.dump(dicc_json, file, indent=2)

        my_order = order_manager.OrderManager()
        value = my_order.send_product("0000000000000000000000000000000000000000000000000000000000000000")
        self.assertEqual(False, value)
    def test_f3_vt6(self):
        """bucle 5 veces"""
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex1 = {"_OrderShipping__alg": "SHA-256",
                    "_OrderShipping__type": "DS",
                    "_OrderShipping__product_id": "8421691423220",
                    "_OrderShipping__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4",
                    "_OrderShipping__delivery_email": "adrian@gmail.com",
                    "_OrderShipping__issued_at": -2208974400.0,
                    "_OrderShipping__delivery_day": -2208888000.0,
                    "_OrderShipping__tracking_code": "5856fbd8f18ad8381d45e0efe946025037a3dfe689f285c1dab0b48ef91df0f0"}
        dicc_json.append(order_ex1)

        order_ex2 ={"_OrderShipping__alg": "SHA-256",
                    "_OrderShipping__type": "DS",
                    "_OrderShipping__product_id": "8421691423220",
                    "_OrderShipping__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4",
                    "_OrderShipping__delivery_email": "adrian@gmail.com",
                    "_OrderShipping__issued_at": -2208974400.0,
                    "_OrderShipping__delivery_day": -2208888000.0,
                    "_OrderShipping__tracking_code": "5856fbd8f18ad8381d45e0efe946025037a3dfe689f285c1dab0b48ef91df0f0"}
        dicc_json.append(order_ex2)

        order_ex3 = {"_OrderShipping__alg": "SHA-256",
                     "_OrderShipping__type": "DS",
                     "_OrderShipping__product_id": "8421691423220",
                     "_OrderShipping__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4",
                     "_OrderShipping__delivery_email": "adrian@gmail.com",
                     "_OrderShipping__issued_at": -2208974400.0,
                     "_OrderShipping__delivery_day": -2208888000.0,
                     "_OrderShipping__tracking_code": "5856fbd8f18ad8381d45e0efe946025037a3dfe689f285c1dab0b48ef91df0f0"}
        dicc_json.append(order_ex3)

        order_ex4 = {"_OrderShipping__alg": "SHA-256",
                     "_OrderShipping__type": "DS",
                     "_OrderShipping__product_id": "8421691423220",
                     "_OrderShipping__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4",
                     "_OrderShipping__delivery_email": "adrian@gmail.com",
                     "_OrderShipping__issued_at": -2208974400.0,
                     "_OrderShipping__delivery_day": -2208888000.0,
                     "_OrderShipping__tracking_code": "5856fbd8f18ad8381d45e0efe946025037a3dfe689f285c1dab0b48ef91df0f0"}
        dicc_json.append(order_ex4)

        order_ex5 = {"_OrderShipping__alg": "SHA-256",
                     "_OrderShipping__type": "DS",
                     "_OrderShipping__product_id": "8421691423220",
                     "_OrderShipping__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4",
                     "_OrderShipping__delivery_email": "adrian@gmail.com",
                     "_OrderShipping__issued_at": -2208974400.0,
                     "_OrderShipping__delivery_day": -2208888000.0,
                     "_OrderShipping__tracking_code": "5856fbd8f18ad8381d45e0efe946025037a3dfe689f285c1dab0b48ef91df0f0"}
        dicc_json.append(order_ex5)

        with open(store_path + "/Almacenf2.JSON", "w", encoding="utf-8", newline="") as file:
            json.dump(dicc_json, file, indent=2)

        my_order = order_manager.OrderManager()
        value = my_order.send_product("0000000000000000000000000000000000000000000000000000000000000000")
        self.assertEqual(False, value)