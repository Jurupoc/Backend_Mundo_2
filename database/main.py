import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./serviceAccountKey.json")

firebase_admin.initialize_app(cred)

db = firestore.client()  # this connects to our Firestore database
collection = db.collection('accounts')  # opens 'accounts' collection
doc = collection.document('new_user')  # specifies the 'rome' document
