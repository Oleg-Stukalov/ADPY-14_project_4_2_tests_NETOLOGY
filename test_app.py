import unittest
from app import get_doc_owner_name, show_all_docs_info, add_new_doc, delete_doc, remove_doc_from_shelf, append_doc_to_shelf, update_date, documents, check_document_existance

NL = '\n'

class TestFunctions(unittest.TestCase):

    #setUp method is overridden from the parent class TestCase
    def setUp(self):
        pass
        #update_date()
        #self.user_doc_number() = user_doc_number()
        #self.functions = Functions_5_1()

    #Each test method starts with the keyword test_
    def test_get_doc_owner_name(self):  # P
        user_doc_number = '2207 876234'
        print('Для теста скопируйте значение: 2207 876234')
        self.assertEqual(get_doc_owner_name(), 'Василий Гупкин')
        user_doc_number2 = '11-2'
        print('Для теста скопируйте значение: 11-2')
        self.assertEqual(get_doc_owner_name(), 'Геннадий Покемонов')
        user_doc_number3 = '10006'
        print('Для теста скопируйте значение: 10006')
        self.assertEqual(get_doc_owner_name(), 'Аристарх Павлов')


    def test_add_new_doc(self):  # A
        print('Для теста скопируйте значение номера: 123')
        print('Для теста скопируйте значение типа: INN')
        print('Для теста скопируйте значение имени: Ivan Petrov')
        print('Для теста скопируйте значение полки: 10')
        new_doc_shelf_number = '10'
        # new_doc_shelf_number = '10'
        # new_doc = {
        #     "type": 'INN',
        #     "number": '123',
        #     "name": 'Ivan Petrov'
        # }
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
        self.assertEqual(check_document_existance(new_doc_number), True)

        # удаляем, что только что создали и проверяем, что оно удалилось
        print('Для теста скопируйте значение номера: 123')
        self.assertEqual(delete_doc(), (new_doc_number, True))
        #delete_doc(new_doc_number)

                # проверяем, что оно удалилось
                #self.assertEqual(check_document_existance(new_doc_number), False)

    def test_show_all_docs_info(self):  # L
        new_doc_number = '2207 876234'
        new_doc_number2 = '11-2'
        new_doc_number3 = '10006'

        self.assertEqual(check_document_existance(new_doc_number), True)
        self.assertEqual(check_document_existance(new_doc_number2), True)
        self.assertEqual(check_document_existance(new_doc_number3), True)


# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()
