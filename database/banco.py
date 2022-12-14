from database.main import db, collection, collection_cliente, collection_prestador


class FireBaseMethods:
    def __init__(self, _db, _collection, ):
        self.firebase = _db
        self.collection = _collection

    def read(self, _document: str = None, ):
        if _document:
            data = self.collection.document(_document).get()
            return data.to_dict()
        all_data = [data.to_dict() for data in self.collection.stream()]
        return all_data

    def read_by_field(self, _field: str, _field_value: str, ):
        doc = self.collection.where(_field, '==', _field_value).limit_to_last(1).get()
        return doc[0].to_dict() if doc else None

    def get_last_id(self, ):
        doc = self.collection.order_by("id").get()
        return doc[-1].to_dict()['id'] if doc else 0

    def create(self, _data: dict, ):
        self.collection.document(_data["email"]).set(_data)
        return _data

    def delete(self, _data: dict, ):
        self.collection.document(_data["email"]).delete()

    def update(self, _document: str, _field: str, _new_value: str):
        self.collection.document(_document).update({_field: _new_value})


firebase_db = FireBaseMethods(db, collection)
firebase_db_cliente = FireBaseMethods(db, collection_cliente)
firebase_db_prestador = FireBaseMethods(db, collection_prestador)
