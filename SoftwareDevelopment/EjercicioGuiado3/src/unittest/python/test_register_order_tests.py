"""class for testing the regsiter_order method"""
import json
import unittest
import os
from freezegun import freeze_time
from uc3m_logistics import order_manager, order_management_exception

path = os.path.dirname(__file__)[:-15]
path += "json/Almacen.JSON"
print(path)
@freeze_time("01-01-2000")
class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""
    def setUp(self) -> None:
        a = order_manager.OrderManager()
        file_store = a.store_path + "/Almacen.JSON"
        if os.path.isfile(file_store):
            os.remove(file_store)

    @freeze_time("01-01-2000 00:00:00")
    def test_f1_Vt1(self):

        my_order = order_manager.OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("e39ed19e25d6c4f0b2ed5bf610e043b4",value)

        with(open(path, "r", encoding="utf-8", newline=""))as file:
            data_list = json.load(file)
        found = False

        if data_list[-1]["_OrderRequest__order_id"] == value:
            found = True
        self.assertTrue(found)

    def test_f1_NVt1(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("842169142322A", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("Exception: Product Id not valid", cm.exception.message)

    def test_f1_NVt2(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423225", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("Exception: Product Id not valid", cm.exception.message)

    def test_f1_NVt3(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("80421691423220", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("Exception: Product Id not valid", cm.exception.message)

    def test_f1_NVt4(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("842169142322", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("Exception: Product Id not valid", cm.exception.message)

    def test_f1_NVt5(self):

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order(8421691423220, "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("Exception: Product Id type not valid", cm.exception.message)
    def test_f1_Vt2(self):
        my_order = order_manager.OrderManager()
        value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("b24ae6e546d46edb1434ffb6f2ed1d04",value)

        with(open(path, "r", encoding="utf-8", newline="")) as file:
            data_list = json.load(file)
        found = False

        if data_list[-1]["_OrderRequest__order_id"] == value:
            found = True
        self.assertTrue(found)
    def test_f1_NVt6(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "OTHER", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("Exception: orderType not valid", cm.exception.message)

    def test_f1_NVt7(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", 7, "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("Exception: orderType type not valid", cm.exception.message)

    def test_f1_Vt3(self):
        my_order = order_manager.OrderManager()
        value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4,MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("9771ea21d3be1cfad82db7309d9be5c1",value)

        with(open(path, "r", encoding="utf-8", newline="")) as file:
            data_list = json.load(file)
        found = False

        if data_list[-1]["_OrderRequest__order_id"] == value:
            found = True
        self.assertTrue(found)
    def test_f1_NVt8(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4,MADRID,SPAIN", "123456789", "28005")
        self.assertEqual("Exception : address not valid", cm.exception.message)

    def test_f1_Vt4(self):
        my_order = order_manager.OrderManager()
        value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBO MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("0c1ef9fc5cab6b45651eb3f48b3b56bb", value)

        with(open(path, "r", encoding="utf-8", newline="")) as file:
            data_list = json.load(file)
        found = False

        if data_list[-1]["_OrderRequest__order_id"] == value:
            found = True
        self.assertTrue(found)

    def test_f1_Vt5(self):
        my_order = order_manager.OrderManager()
        value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("6e2eb61bfb1f720e5e18950bf43260bb", value)

        with(open(path, "r", encoding="utf-8", newline="")) as file:
            data_list = json.load(file)
        found = False

        if data_list[-1]["_OrderRequest__order_id"] == value:
            found = True
        self.assertTrue(found)

    def test_f1_Vt6(self):
        my_order = order_manager.OrderManager()
        value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4, MADRID, SPAINaaaaaaaaaaaaaaaaaaaaa"
                                                                        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                                                        "aaaaaaa", "123456789", "28005")
        self.assertEqual("d7b99460d58caa26d99a563134004496", value)

        with(open(path, "r", encoding="utf-8", newline="")) as file:
            data_list = json.load(file)
        found = False

        if data_list[-1]["_OrderRequest__order_id"] == value:
            found = True
        self.assertTrue(found)

    def test_f1_Vt7(self):
        my_order = order_manager.OrderManager()
        value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4, MADRID, SPAINaaaaaaaaaaaaaaaaaaaaaaaaa"
                                                                    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaAaa"
                                                                    , "123456789", "28005")
        self.assertEqual("c602a0b664c76cedbe41e51198cbe6d7", value)

        with(open(path, "r", encoding="utf-8", newline="")) as file:
            data_list = json.load(file)
        found = False

        if data_list[-1]["_OrderRequest__order_id"] == value:
            found = True
        self.assertTrue(found)

    def test_f1_NVt9(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "BOA,4, MADRID, PAIN", "123456789", "28005")
        self.assertEqual("Exception : address not valid", cm.exception.message)

    def test_f1_NVt10(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAINaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                                                , "123456789", "28005")
        self.assertEqual("Exception : address not valid", cm.exception.message)

    def test_f1_NVt11(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", 42, "123456789", "28005")
        self.assertEqual("Exception : address type not valid", cm.exception.message)

    def test_f1_NVt12(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "12345678", "28005")
        self.assertEqual("Exception : phone_number not valid", cm.exception.message)

    def test_f1_NVt13(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "1234567890", "28005")
        self.assertEqual("Exception : phone_number not valid", cm.exception.message)

    def test_f1_NVt14(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", 123456789, "28005")
        self.assertEqual("Exception : phone_number type not valid", cm.exception.message)

    def test_f1_NVt15(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "12345A789", "28005")
        self.assertEqual("Exception : phone_number not valid", cm.exception.message)

    def test_f1_NVt16(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", "2800")
        self.assertEqual("Exception : zipcode not valid", cm.exception.message)

    def test_f1_NVt17(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", "280051")
        self.assertEqual("Exception : zipcode not valid", cm.exception.message)

    def test_f1_NVt18(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", "53005")
        self.assertEqual("Exception : zipcode not valid", cm.exception.message)

    def test_f1_NVt19(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", "2A005")
        self.assertEqual("Exception : zipcode not valid", cm.exception.message)

    def test_f1_NVt20(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", 28991)
        self.assertEqual("Exception : zipcode type not valid", cm.exception.message)


if __name__ == '__main__':
    unittest.main()