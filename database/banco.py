from main import db, cred, collection
import json


class FireBaseMethods:
    def __init__(self, ):
        self.firebase = db
        self.collection = collection
        self.cred = cred

    def read(self, _collection: str, _document: str, ):
        doc = self.collection(_collection).document(_document).get()
        return json.loads(doc.to_dict())

    def create(self, _collection: str, data, _document: str, ):
        self.collection(_collection).document(_document).set(data)

    def delete(self, _collection: str, _document: str, ):
        self.collection(_collection).document(_document).delete()

    def delete_field(self, _collection: str, _document: str, _field: str, ):
        doc_ref = self.collection(_collection)
        doc_ref.update({_field: self.firebase.DELETE_FIELD})

    def update(self, _collection: str, _document: str, _field: str, _new_value: str):
        self.collection(_collection).document(_document).update({_field: _new_value})
