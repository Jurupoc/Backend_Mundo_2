from flask import Flask, request, jsonify
from database.servicos.servicos import firebase_service_instance, UserAlreadyCreated, UserNotFound

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/user", methods=['POST'])
def post():
    try:
        user_data = request.json
        message, status_code = firebase_service_instance.create_new_user(user_data)
        return jsonify({
                        'message': message,
                        'status_code': status_code
                        })

    except UserAlreadyCreated as error:
        return jsonify({
                        'message': error.message,
                        'status_code': error.status_code
                        })


@app.route("/user", methods=['GET'])
def get_all():
    try:
        data = firebase_service_instance.get_all_user()
        return jsonify(data)
    except Exception as e:
        return f"[ERRO]: {e}"


@app.route("/user/login", methods=['GET'])
def login():
    try:
        user_data = request.json
        message = firebase_service_instance.log_in(user_data)
        return jsonify(message)

    except UserNotFound as error:
        return jsonify({
            'message': error.message,
            'status_code': error.status_code
        })