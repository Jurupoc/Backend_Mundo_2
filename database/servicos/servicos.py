from database.banco.banco import firebase_db, FireBaseMethods
import json

class ServiceException(Exception):
    """Base class for other exceptions"""
    pass


class UserAlreadyCreated(ServiceException):
    """Raised when a User is already in the data base"""
    def __init__(self):
        self.message = 'Usuário ja cadastrado'
        self.status_code = 200


class UserNotFound(ServiceException):
    """Raised when a User is not found in the data base"""
    def __init__(self):
        self.message = 'Dados informados não correspondem a nenhum usuário cadastrado.'
        self.status_code = 200


class FirebaseServices:
    def __init__(self, db_reference: FireBaseMethods):
        self.db: FireBaseMethods = db_reference
        self.collection = "accounts"

    def get_all_user(self, ) -> list:
        data = self.db.read()
        return data

    def get_user_by_email(self, user_email: str, ) -> dict:
        data = self.db.read_by_field('email', user_email)
        if not data:
            raise UserNotFound()
        return data

    def create_new_user(self, user_data: dict, ):
        verificacao = self.db.read_by_field('email', user_data['email'])
        if not verificacao:
            self.db.create(user_data['email'], user_data)
            return {'message': 'Usuário Criado', 'status_code': 200}
        raise UserAlreadyCreated()

    def log_in(self, user_data: dict, ):
        data = self.db.read('email', user_data['email'])
        if data and data['password'] == user_data['password']:
            return {'message': 'Login realizado', 'status_code': 200}
        raise UserNotFound()

    def delete_user(self, user_email: str, ):
        doc = self.db.read(user_email)
        if doc:
            self.db.delete(user_email)
            return {'message': 'Usurio deletado', 'status_code': 200}
        raise UserNotFound



firebase_service_instance = FirebaseServices(firebase_db)