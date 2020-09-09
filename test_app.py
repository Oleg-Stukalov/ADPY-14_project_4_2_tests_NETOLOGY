import unittest
from app import get_doc_owner_name, show_all_docs_info, add_new_doc, delete_doc, remove_doc_from_shelf, append_doc_to_shelf, update_date, documents

NL = '\n'

class TestFunctions(unittest.TestCase):

    #setUp method is overridden from the parent class TestCase
    def setUp(self):
        update_date()
        #self.user_doc_number() = user_doc_number()
        #self.functions = Functions_5_1()

    #Each test method starts with the keyword test_
    def test_get_doc_owner_name(self):  # P
        user_doc_number = '2207 876234'
        self.assertEqual(get_doc_owner_name(user_doc_number), 'Василий Гупкин')
        user_doc_number2 = '11-2'
        self.assertEqual(get_doc_owner_name(user_doc_number2), 'Геннадий Покемонов')
        user_doc_number3 = '10006'
        self.assertEqual(get_doc_owner_name(user_doc_number3), 'Аристарх Павлов')


    def test_add_new_doc(self):  # A
        new_doc_shelf_number = '10'
        new_doc = {
            "type": 'INN',
            "number": '123',
            "name": 'Ivan Petrov'
        }
        self.assertEqual(add_new_doc(), new_doc_shelf_number)

    def test_delete_doc(self):
        # создадим, чтобы было что удалять
        new_doc = {
            "type": 'INN',
            "number": '123',
            "name": 'Ivan Petrov'
        }

        new_doc_number = '123'
        new_doc_shelf_number = '10'

        documents.append(new_doc)
        append_doc_to_shelf(new_doc_number, new_doc_shelf_number)

        # проверяем, что оно создалось
        assert is_created

        # удаляем, что только что создали
        new_doc_number = '123'
        delete_doc(new_doc_number)

        # проверяем, что оно удалилось
        assert is_deleted

    # def test_delete_doc(self):  # D
    #     user_doc_number = '123'
    #     delete_doc()
    #     self.assertEqual(remove_doc_from_shelf(user_doc_number), user_doc_number)

    def test_show_all_docs_info(self):  # L
        self.assertEqual(show_all_docs_info(), ('passport "2207 876234" "Василий Гупкин" NL', 'invoice "11-2" "Геннадий Покемонов" NL', 'insurance "10006" "Аристарх Павлов"'))


# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()
