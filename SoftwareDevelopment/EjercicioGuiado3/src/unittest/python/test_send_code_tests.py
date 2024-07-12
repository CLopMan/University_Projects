"""class for testing the regsiter_order method"""
import json
import unittest
import os
from freezegun import freeze_time
from uc3m_logistics import order_manager, order_management_exception


store_path = os.path.dirname(__file__)[:-15] + "json"
print("path: " + store_path)

@freeze_time("01-01-2000")
class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""
    def setUp(self) -> None:
        if os.path.isfile(store_path + "/Almancen.JSON"):
            print("por aquí pasa")
            os.remove(store_path + "/Almacen.JSON")
        if os.path.isfile(store_path + "/Almacenf2.JSON"):
            os.remove(store_path + "/Almacenf2.JSON")
    @freeze_time("01-01-2000 00:00:00")
    def test_f2_Vt1(self):
        input_file = store_path + "/f2_vt1.json"

        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        #### Falta borrar y crear el almacen
        my_order = order_manager.OrderManager()
        ########## Falta dar la dirección del json
        value = my_order.send_code(input_file)
        self.assertEqual("5856fbd8f18ad8381d45e0efe946025037a3dfe689f285c1dab0b48ef91df0f0",value)

    def test_f2_NVt1(self):
        """Duplicación de format"""
        input_file = store_path + "/f2_nvt1.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm_ex.exception.message)

    def test_f2_NVt2(self):
        """deletion de format"""
        input_file = store_path + "/f2_nvt2.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm_ex.exception.message)

    def test_f2_NVt3(self):
        """duplication de llavein"""
        input_file = store_path + "/f2_nvt3.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm_ex.exception.message)

    def test_f2_NVt4(self):
        """deletion de llavein"""
        input_file = store_path + "/f2_nvt4.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm_ex.exception.message)

    def test_f2_NVt5(self):
        """dup de datos"""
        input_file = store_path + "/f2_nvt5.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm_ex.exception.message)

    def test_f2_NVt6(self):
        """del de datos"""
        input_file = store_path + "/f2_nvt6.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("There are too/few keys", cm_ex.exception.message)

    def test_f2_NVt7(self):
        """dup llavefin"""
        input_file = store_path + "/f2_nvt7.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm_ex.exception.message)

    def test_f2_NVt8(self):
        """del llavefin"""
        input_file = store_path + "/f2_nvt8.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm_ex.exception.message)

    def test_f2_NVt9(self):
        """mod de llave inicio"""
        input_file = store_path + "/f2_nvt9.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm_ex.exception.message)

    def test_f2_NVt10(self):
        """dup de parte1"""
        input_file = store_path + "/f2_nvt10.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm_ex.exception.message)

    def test_f2_NVt11(self):
        """del de parte1"""
        input_file = store_path + "/f2_nvt11.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("There are too/few keys", cm_ex.exception.message)

    def test_f2_NVt12(self):
        """dup de comma"""
        input_file = store_path + "/f2_nvt12.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm_ex.exception.message)
    def test_f2_NVt13(self):
        """del de comma"""
        input_file = store_path + "/f2_nvt13.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm_ex.exception.message)

    def test_f2_nvt14(self):
        """dup de parte2"""
        input_file = store_path + "/f2_nvt14.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm_ex.exception.message)
    def test_f2_nvt15(self):
        """del de parte2"""
        input_file = store_path + "/f2_nvt15.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("There are too/few keys", cm_ex.exception.message)

    def test_f2_nvt16(self):
        """mod de }"""
        input_file = store_path + "/f2_nvt16.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm_ex.exception.message)

    def test_f2_nvt17(self):
        """dup etiqueta1"""
        input_file = store_path + "/f2_nvt17.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm_ex.exception.message)

    def test_f2_nvt18(self):
        """del etiqueta1"""
        input_file = store_path + "/f2_nvt18.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm_ex.exception.message)

    def test_f2_nvt19(self):
        """dup separador"""
        input_file = store_path + "/f2_nvt19.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm_ex.exception.message)

    def test_f2_nvt20(self):
        """del separador"""
        input_file = store_path + "/f2_nvt20.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm_ex.exception.message)

    def test_f2_nvt21(self):
        """dup dato1"""
        input_file = store_path + "/f2_nvt21.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm_ex.exception.message)

    def test_f2_nvt22(self):
        """del dato1"""
        input_file = store_path + "/f2_nvt22.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm_ex.exception.message)

    def test_f2_nvt23(self):
        """mod coma"""
        input_file = store_path + "/f2_nvt23.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm_ex.exception.message)

    def test_f2_nvt24(self):
        """dup etiqueta2"""
        input_file = store_path + "/f2_nvt24.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm_ex.exception.message)

    def test_f2_nvt25(self):
        """dup separador"""
        input_file = store_path + "/f2_nvt25.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm_ex.exception.message)

    def test_f2_nvt26(self):
        """dup separador"""
        input_file = store_path + "/f2_nvt26.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm_ex.exception.message)

    def test_f2_nvt27(self):
        """dup separador"""
        input_file = store_path + "/f2_nvt27.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm_ex.exception.message)

    def test_f2_nvt28(self):
        """dup separador"""
        input_file = store_path + "/f2_nvt28.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm_ex.exception.message)

    def test_f2_nvt29(self):
        """dup separador"""
        input_file = store_path + "/f2_nvt29.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm_ex.exception.message)

    def test_f2_nvt30(self):
        """dup separador"""
        input_file = store_path + "/f2_nvt30.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("Incorrect keys", cm_ex.exception.message)

    def test_f2_nvt31(self):
        """dup separador"""
        input_file = store_path + "/f2_nvt31.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("Incorrect keys", cm_ex.exception.message)

    def test_f2_nvt32(self):
        """dup separador"""
        input_file = store_path + "/f2_nvt32.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm_ex.exception.message)

    def test_f2_nvt33(self):
        """dup separador"""
        input_file = store_path + "/f2_nvt33.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("Wrong Hash", cm_ex.exception.message)
    def test_f2_nvt34(self):
        """dup separador"""
        input_file = store_path + "/f2_nvt34.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("Wrong Hash", cm_ex.exception.message)

    def test_f2_nvt35(self):
        """dup separador"""
        input_file = store_path + "/f2_nvt35.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("Incorrect keys", cm_ex.exception.message)

    def test_f2_nvt36(self):
        """dup separador"""
        input_file = store_path + "/f2_nvt36.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("Incorrect keys", cm_ex.exception.message)

    def test_f2_nvt37(self):
        """dup separador"""
        input_file = store_path + "/f2_nvt37.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm_ex.exception.message)

    def test_f2_vt2(self):
        input_file = store_path + "/f2_vt2.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        #### Falta borrar y crear el almacen
        my_order = order_manager.OrderManager()
        ########## Falta dar la dirección del json
        value = my_order.send_code(input_file)
        self.assertEqual("5856fbd8f18ad8381d45e0efe946025037a3dfe689f285c1dab0b48ef91df0f0", value)

    def test_f2_nvt38(self):
        """del idmail"""
        input_file = store_path + "/f2_nvt38.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("Wrong Contact Email", cm_ex.exception.message)

    def test_f2_nvt39(self):
        """dup arroba"""
        input_file = store_path + "/f2_nvt39.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("Wrong Contact Email", cm_ex.exception.message)
    def test_f2_nvt40(self):
        """del @"""
        input_file = store_path + "/f2_nvt40.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("Wrong Contact Email", cm_ex.exception.message)

    def test_f2_vt3(self):
        """dup dominio"""
        input_file = store_path + "/f2_vt3.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        #### Falta borrar y crear el almacen
        my_order = order_manager.OrderManager()
        ########## Falta dar la dirección del json
        value = my_order.send_code(input_file)
        self.assertEqual("5856fbd8f18ad8381d45e0efe946025037a3dfe689f285c1dab0b48ef91df0f0", value)

    def test_f2_nvt41(self):
        """del dominio"""
        input_file = store_path + "/f2_nvt41.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("Wrong Contact Email", cm_ex.exception.message)

    def test_f2_nvt42(self):
        """dup ."""
        input_file = store_path + "/f2_nvt42.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("Wrong Contact Email", cm_ex.exception.message)

    def test_f2_nvt43(self):
        """del ."""
        input_file = store_path + "/f2_nvt43.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("Wrong Contact Email", cm_ex.exception.message)

    def test_f2_nvt44(self):
        """mod ."""
        input_file = store_path + "/f2_nvt44.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("Wrong Contact Email", cm_ex.exception.message)

    def test_f2_vt4(self):
        """dup extension"""
        input_file = store_path + "/f2_vt4.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        #### Falta borrar y crear el almacen
        my_order = order_manager.OrderManager()
        ########## Falta dar la dirección del json
        value = my_order.send_code(input_file)
        self.assertEqual("5856fbd8f18ad8381d45e0efe946025037a3dfe689f285c1dab0b48ef91df0f0", value)
    def test_f2_nvt45(self):
        """del extension """
        input_file = store_path + "/f2_nvt45.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("Wrong Contact Email", cm_ex.exception.message)

    def test_f2_nvt46(self):
        """mod \" """
        input_file = store_path + "/f2_nvt46.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm_ex.exception.message)

    def test_f2_nvt47(self):
        """mod OrderID """
        input_file = store_path + "/f2_nvt47.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("Incorrect keys", cm_ex.exception.message)

    def test_f2_nvt48(self):
        """mod id """
        input_file = store_path + "/f2_nvt48.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("Wrong Hash", cm_ex.exception.message)

    def test_f2_nvt49(self):
        """mod ContactEmail"""
        input_file = store_path + "/f2_nvt49.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("Incorrect keys", cm_ex.exception.message)

    def test_f2_nvt50(self):
        """mod email"""
        input_file = store_path + "/f2_nvt50.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("Wrong Contact Email", cm_ex.exception.message)

    def test_f2_nvt51(self):
        """mod @"""
        input_file = store_path + "/f2_nvt51.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("Wrong Contact Email", cm_ex.exception.message)

    def test_f2_nvt52(self):
        """mod dominio"""
        input_file = store_path + "/f2_nvt52.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("Wrong Contact Email", cm_ex.exception.message)

    def test_f2_nvt53(self):
        """mod extension"""
        input_file = store_path + "/f2_nvt53.json"
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm_ex:
            my_order.send_code(input_file)
        self.assertEqual("Wrong Contact Email", cm_ex.exception.message)

if __name__ == '__main__':
    unittest.main()