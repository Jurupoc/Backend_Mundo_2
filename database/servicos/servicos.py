from database.banco.banco import firebase_db, FireBaseMethods
import json

class FirebaseServices:
    def __init__(self, db_reference: FireBaseMethods):
        self.db: FireBaseMethods = db_reference
        self.collection = "accounts"

    def get_all_user(self, ) -> list:
        data = self.db.read()
        return data

    def get_user_by_email(self, user_email: str, ) -> dict:
        data = self.db.read_by_field('email', user_email)
        return data

    def create_new_user(self, user_data: dict, ):
        verificacao = self.db.read_by_field('email', user_data['email'])
        if not verificacao:
            self.db.create(user_data['email'], user_data)
            return 'Usuário criado', 200
        return 'Usuário já cadastrado', 200

    def log_in(self, user_data: dict, ):
        data = self.db.read('email', user_data['email'])
        if data and data['password'] == user_data['password']:
            return 'Login realizado', 200
        return 'Dados incorretos', 401

    def delete_user(self, user_email: str, ):
        doc = self.db.read(user_email)
        if doc:
            self.db.delete(user_email)
            return 'Registro deletado', 200
        return 'Registro não encontrado', 401


firebase_service_instance = FirebaseServices(firebase_db)