from main import db, collection
import json


class FireBaseMethods:
    def __init__(self, _db, _collection, ):
        self.firebase = _db
        self.collection = _collection

    def read_by_document(self, _document: str, ):
        doc = self.collection.document(_document).get()
        return doc.to_dict()

    def read_by_field(self, _field: str, _field_value: str):
        docs = self.collection.where(_field, '==', _field_value).stream()
        return [doc.to_dict() for doc in docs][0]

    def create(self, _document: str, data: dict, ):
        self.collection.document(_document).set(data)

    def delete(self, _document: str, ):
        self.collection.document(_document).delete()

    def update(self, _document: str, _field: str, _new_value: str):
        self.collection.document(_document).update({_field: _new_value})


firebase_db = FireBaseMethods(db, collection)
