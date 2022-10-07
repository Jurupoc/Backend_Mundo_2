import unittest
from banco import firebase_db


class TesteDbMethods(unittest.TestCase):

    def setUp(self) -> None:
        self.db = firebase_db
        self.teste_doc = 'test_user@email.com'

    def test_create_and_read_document_method(self):
        user_data = {
            'email': 'test_user@email.com',
            'id': '-1',
            'idCliente': 0,
            'idPrestador': 0,
            'password': '123456'
        }

        self.db.create(self.teste_doc, user_data)
        self.assertEqual(self.db.read_by_document(self.teste_doc), user_data)

    def test_delete_by_email_method(self):
        user_data = {
            'email': 'test_user@email.com',
            'id': '-1',
            'idCliente': 0,
            'idPrestador': 0,
            'password': '123456'
        }

        self.db.create(self.teste_doc, user_data)
        self.assertEqual(self.db.read_by_document(self.teste_doc), user_data)  # Verifica se o registro foi criado

        self.db.delete(self.teste_doc)
        self.assertEqual(self.db.read_by_document(self.teste_doc), None)  # Verifica se o registro foi deletado

    def test_read_by_field_method(self):
        user_data = {
            'email': 'test_user@email.com',
            'id': '-1',
            'idCliente': 0,
            'idPrestador': 0,
            'password': '123456'
        }

        self.db.create(self.teste_doc, user_data)
        self.assertEqual(self.db.read_by_document(self.teste_doc), user_data)  # Verifica se o registro foi criado

        self.assertEqual(self.db.read_by_field('email', 'test_user@email.com'), user_data)

    def tearDown(self):
        self.db.delete(self.teste_doc)


if __name__ == '__main__':
    unittest.main()
