import unittest
from database.servicos.servicos import firebase_service_instance


class TesteServiceMethods(unittest.TestCase):

    def setUp(self) -> None:
        self.services_instance = firebase_service_instance
        self.teste_email = 'test_user@email.com'

    def test_get_all_users(self):
        user_data = {
            'email': self.teste_email,
            'id': '1',
            'idCliente': 0,
            'idPrestador': 0,
            'password': '123456'
        }

        self.services_instance.create_new_user(user_data)
        self.assertNotEqual(self.services_instance.get_all_user(), [])

    def test_create_new_user(self):
        user_data = {
            'email': 'test_user@email.com',
            'id': '-1',
            'idCliente': 0,
            'idPrestador': 0,
            'password': '123456'
        }

        self.services_instance.create_new_user(user_data)
        self.assertEqual(self.services_instance.get_user_by_email(user_data['email']), user_data)

    def test_delete_user(self):
        user_data = {
            'email': 'test_user@email.com',
            'id': '-1',
            'idCliente': 0,
            'idPrestador': 0,
            'password': '123456'
        }

        self.services_instance.create_new_user(user_data)
        self.assertEqual(self.services_instance.get_user_by_email(user_data['email']), user_data)

        self.services_instance.delete_user(user_data['email'])
        self.assertEqual(self.services_instance.get_user_by_email(user_data['email']), None)

    def tearDown(self):
        self.services_instance.delete_user(self.teste_email)


if __name__ == '__main__':
    unittest.main()
