import unittest
from database.banco import firebase_db


class TesteDbMethods(unittest.TestCase):

    def setUp(self) -> None:
        self.db = firebase_db
        self.test_user = {
            'email': 'test_user@email.com',
            'id': '-1',
            'idCliente': 0,
            'idPrestador': 0,
            'password': '123456'
        }

    def test_read_all_method(self):
        user_data = self.test_user

        self.db.create(user_data['email'], user_data)
        self.assertNotEqual(self.db.read(), [])

    def test_create_and_read_document_method(self):
        user_data = user_data = self.test_user

        self.db.create(user_data['email'], user_data)
        self.assertEqual(self.db.read(user_data['email']), user_data)

    def test_delete_by_email_method(self):
        user_data = user_data = self.test_user

        self.db.create(user_data['email'], user_data)
        self.assertEqual(self.db.read(user_data['email']), user_data)  # Verifica se o registro foi criado

        self.db.delete(user_data['email'])
        self.assertEqual(self.db.read(user_data['email']), None)  # Verifica se o registro foi deletado

    def test_read_by_field_method(self):
        user_data = user_data = self.test_user

        self.db.create(user_data['email'], user_data)
        self.assertEqual(self.db.read(user_data['email']), user_data)  # Verifica se o registro foi criado

        self.assertEqual(self.db.read_by_field('email', user_data['email']), user_data)

    def test_update_method(self):
        user_data = self.test_user

        self.db.create(user_data['email'], user_data)
        self.assertEqual(self.db.read(user_data['email'])['id'], user_data['id'])  # Verifica se o registro foi criado

        self.db.update(user_data['email'], 'id', 666)
        self.assertEqual(self.db.read(user_data['email'])['id'], 666)  # Verifica se o registro foi deletado

    def tearDown(self):
        self.db.delete(self.test_user['email'])


if __name__ == '__main__':
    unittest.main()
