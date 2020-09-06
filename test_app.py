import unittest
from unittest.mock import patch
from app import get_doc_owner_name, show_all_docs_info, add_new_doc, delete_doc, remove_doc_from_shelf

class TestFunctions(unittest.TestCase):

    #setUp method is overridden from the parent class TestCase
    def setUp(self):
        pass
        #self.user_doc_number() = user_doc_number()
        #self.functions = Functions_5_1()

    #Each test method starts with the keyword test_
    def test_get_doc_owner_name(self):  # P
        user_doc_number = '2207 876234'
        self.assertEqual(get_doc_owner_name(), 'Василий Гупкин')
        user_doc_number2 = '11-2'
        self.assertEqual(get_doc_owner_name(), 'Геннадий Покемонов')
        user_doc_number3 = '10006'
        self.assertEqual(get_doc_owner_name(), 'Аристарх Павлов')

    def test_show_all_docs_info(self):  # L
        self.assertEqual(show_all_docs_info(), ('passport "2207 876234" "Василий Гупкин"', 'invoice "11-2" "Геннадий Покемонов"', 'insurance "10006" "Аристарх Павлов"'))


    def test_add_new_doc(self):  # A
        new_doc_number = '123'
        new_doc_type = 'INN'
        new_doc_owner_name = 'Ivan Petrov'
        new_doc_shelf_number = '10'
        add_new_doc()

        user_doc_number4 = '123'
        self.assertEqual(get_doc_owner_name(), 'Ivan Petrov')

    def test_delete_doc(self):  # D
        user_doc_number = '123'
        delete_doc()
        self.assertEqual(remove_doc_from_shelf(), '123')


# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()
