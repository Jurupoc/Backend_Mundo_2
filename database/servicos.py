from banco import FireBaseMethods
import json

class FirebaseServices:
    def __init__(self, db_reference: FireBaseMethods):
        self.db = db_reference
        self.collection = "accounts"

    def create_new_user(self, user_data: dict, ):
        verificacao = self.db.read_by_field('email', user_data['email'])
        if not verificacao:
            self.db.create(user_data['email'], user_data)
            return 'Usuário criado', 200
        return 'Usuário já cadastrado', 200

    def log_in(self, user_data: dict, ):
        data = self.db.read_by_field('email', user_data['email'])
        if data and data['password'] == user_data['password']:
            return 'Login realizado', 200
        return 'Dados incorretos', 401

    def delete_user(self, user_data: dict, ):
        doc = self.db.read_by_document(user_data['email'])
        if doc:
            self.db.delete(user_data['email'])
            return 'Registro deletado', 200
        return 'Registro não encontrado', 401


FirebaseServices(FireBaseMethods)