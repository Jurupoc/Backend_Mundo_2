import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("database/serviceAccountKey.json")

firebase_admin.initialize_app(cred)

db = firestore.client()  # this connects to our Firestore database
collection = db.collection('accounts')  # opens 'accounts' collection
collection_cliente = db.collection('Clientes')  # opens 'Clientes' collection
collection_prestador = db.collection('Prestador')  # opens 'Clientes' collection