import unittest
from unittest.mock import patch
from app import get_doc_owner_name, show_all_docs_info, add_new_doc, delete_doc

class TestFunctions(unittest.TestCase):

    #setUp method is overridden from the parent class TestCase
    def setUp(self):
        pass
        #self.functions = Functions_5_1()

    #Each test method starts with the keyword test_
    def test_get_doc_owner_name():  # P
        user_doc_number = input('Введите номер документа - ')
        print()
        doc_exist = check_document_existance(user_doc_number)
        if doc_exist:
            for current_document in documents:
                doc_number = current_document['number']
                if doc_number == user_doc_number:
                    return current_document['name']

    def test_show_all_docs_info():  # L
        print('Список всех документов:\n')
        for current_document in documents:
            show_document_info(current_document)

    def test_add_new_doc():  # A
        new_doc_number = input('Введите номер документа - ')
        new_doc_type = input('Введите тип документа - ')
        new_doc_owner_name = input('Введите имя владельца документа- ')
        new_doc_shelf_number = input('Введите номер полки для хранения - ')
        new_doc = {
            "type": new_doc_type,
            "number": new_doc_number,
            "name": new_doc_owner_name
        }
        documents.append(new_doc)
        append_doc_to_shelf(new_doc_number, new_doc_shelf_number)
        return new_doc_shelf_number

    def test_delete_doc():  # D
        user_doc_number = input('Введите номер документа - ')
        doc_exist = check_document_existance(user_doc_number)
        if doc_exist:
            for current_document in documents:
                doc_number = current_document['number']
                if doc_number == user_doc_number:
                    documents.remove(current_document)
                    remove_doc_from_shelf(doc_number)
                    return doc_number, True

  # def test_people(self):
  #   self.assertEqual(self.functions.number2name('2207 876234'), 'Василий Гупкин')
  #   self.assertEqual(self.functions.number2name('11-2'), 'Геннадий Покемонов')
  #   self.assertEqual(self.functions.number2name('10006'), 'Аристарх Павлов')
  #
  # def test_shelf(self):
  #   self.assertEqual(self.functions.number2shelf('2207 876234'), '1')
  #   self.assertEqual(self.functions.number2shelf('11-2'), '1')
  #   self.assertEqual(self.functions.number2shelf('5455 028765'), '1')
  #   self.assertEqual(self.functions.number2shelf('1006'), '2')
  #
  # def test_list(self):
  #   self.assertEqual(self.functions.list_documents('passport', '2207 876234', 'Василий Гупкин'), True)
  #   self.assertEqual(self.functions.list_documents('invoice', '11-2', 'Геннадий Покемонов'), True)
  #   self.assertEqual(self.functions.list_documents('insurance', '10006', 'Аристарх Павлов'), True)
  #
  # def test_add(self):
  #   self.assertEqual(self.functions.add_document('testdoc', '12345', 'Ivan Petrov', '1'), True)

# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()
