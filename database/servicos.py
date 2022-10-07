from banco import FireBaseMethods
import json

class FirebaseServices:
    def __init__(self, db_reference: FireBaseMethods):
        self.db = db_reference
        self.collection = "accounts"

    def create_new_user(self, user_data: dict, ):
        try:
            self.db.read_by_field()




FirebaseServices(FireBaseMethods)