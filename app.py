from flask import Flask, request, jsonify
from database.servicos import firebase_service_instance

app = Flask(__name__)


@app.route("/user", methods=['POST'])
def post():

        user_data = request.json
        message = firebase_service_instance.create_new_user(user_data)
        return jsonify(message)


@app.route("/user", methods=['GET'])
def get_all():
    data = firebase_service_instance.get_all_user()
    return jsonify(data)


@app.route("/user/login", methods=['GET'])
def login():
    user_data = request.json
    message = firebase_service_instance.log_in(user_data)
    return jsonify(message)
