from database.banco import firebase_db, FireBaseMethods, firebase_db_cliente, firebase_db_prestador


class FirebaseServices:
    def __init__(self, db_reference: FireBaseMethods):
        self.db: FireBaseMethods = db_reference
        self.collection = "accounts"

    def get_all_user(self, ) -> list:
        response = dict()
        response['data'] = self.db.read()
        return response

    def get_user_by_email(self, user_data: dict, ) -> dict:
        response = dict()
        response['data'] = self.db.read_by_field('email', user_data['email'])
        response['message'] = 'Sucesso'

        if not response['data']:
            response['message'] = 'Usuário não encontrado'

        return response

    def get_user_by_id(self, user_data: dict, ) -> dict:
        response = dict()
        response['data'] = self.db.read_by_field('id', user_data['id'])

        if not response['data']:
            response['message'] = 'Usuário não Encontrado'

        return response

    def create_new_user(self, user_data: dict, ) -> dict:
        response = dict()
        verificacao = self.db.read_by_field('email', user_data['email'])

        if not verificacao:
            user_data['id'] = self.db.get_last_id() + 1
            print(f'ID = {self.db.get_last_id()}')
            response['data'] = self.db.create(user_data)

            response['message'] = 'Usuário Criado'
            return response

        response['message'] = 'Usuário ja cadastrado'
        return response

    def log_in(self, user_data: dict, ) -> dict:
        response = dict()
        response['data'] = self.db.read_by_field('email', user_data['email'])

        if not response['data']:
            response['message'] = 'Usuário não encontrado'
            return response

        if not response['data']['password'] == user_data['password']:
            response['message'] = 'Credenciais incorretas'
            return response

        response['message'] = 'Login realizado'
        return response

    def delete_user(self, user_data: dict, ) -> dict:
        response = dict()
        response['data'] = self.db.read(user_data['email'])

        if response['data']:
            self.db.delete(user_data)
            response['message'] = 'Usuário deletado'
            return response

        response['message'] = 'Usuário não encontrado'
        return response

    def reset_password(self, user_data: dict) -> dict:
        response = dict()
        response['data'] = self.db.read(user_data['email'])

        if response['data']:
            self.db.update(user_data['email'], 'password', user_data['new_password'])
            response['message'] = 'Usuário atualizado'
            return response

        response['message'] = 'Usuário não encontrado'
        return response


firebase_service_instance = FirebaseServices(firebase_db)
firebase_service_instance_cliente = FirebaseServices(firebase_db_cliente)
firebase_service_instance_prestador = FirebaseServices(firebase_db_prestador)