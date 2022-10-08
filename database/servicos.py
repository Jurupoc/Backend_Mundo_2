from database.banco import firebase_db, FireBaseMethods


class FirebaseServices:
    def __init__(self, db_reference: FireBaseMethods):
        self.db: FireBaseMethods = db_reference
        self.collection = "accounts"

    def get_all_user(self, ) -> list:
        response = dict()
        response['data'] = self.db.read()
        return response

    def get_user_by_email(self, user_email: str, ) -> dict:
        response = dict()
        response['data'] = self.db.read_by_field('email', user_email)

        if not response['data']:
            response['message'] = 'Usuário não Encontrado'

        return response

    def get_user_by_id(self, user_id: str, ) -> dict:
        response = dict()
        response['data'] = self.db.read_by_field('id', user_id)

        if not response['data']:
            response['message'] = 'Usuário não Encontrado'

        return response

    def create_new_user(self, user_data: dict, ):
        response = dict()
        verificacao = self.db.read_by_field('email', user_data['email'])
        if not verificacao:
            response['data'] = self.db.create(user_data['email'], user_data)
            response['message'] = 'Usuário Criado'
            return response

        response['message'] = 'Usuário ja cadastrado'
        return response

    def log_in(self, user_data: dict, ):
        response = dict()
        response['data'] = self.db.read_by_field('email', user_data['email'])

        if response['data'] and response['data']['password'] == user_data['password']:
            response['message'] = 'Login realizado'
            return response

        response['message'] = 'Usuário não encontrado'
        return response

    def delete_user(self, user_email: str, ):
        response = dict()
        response['data'] = self.db.read(user_email)

        if response['data']:
            self.db.delete(user_email)
            response['message'] = 'Usuário deletado'
            return response

        response['message'] = 'Usuário não encontrado'
        return response



firebase_service_instance = FirebaseServices(firebase_db)