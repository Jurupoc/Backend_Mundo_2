from database.main import db, collection
import json


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
        docs = self.collection.where(_field, '==', _field_value).stream()
        data = [doc.to_dict() for doc in docs]
        return data[0] if data else None

    def create(self, _document: str, data: dict, ):
        self.collection.document(_document).set(data)
        return data

    def delete(self, _document: str, ):
        self.collection.document(_document).delete()

    def update(self, _document: str, _field: str, _new_value: str):
        self.collection.document(_document).update({_field: _new_value})


firebase_db = FireBaseMethods(db, collection)
