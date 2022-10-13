from app import app
from flask import jsonify, request
from database.servicos import firebase_service_instance, firebase_service_instance_cliente, firebase_service_instance_prestador
import scripts.ML as ML

@app.route("/user", methods=['POST'])
def create_user():
    user_data = request.json
    message = firebase_service_instance.create_new_user(user_data)
    return jsonify(message)


@app.route("/user", methods=['GET'])
def get_all_users():
    data = firebase_service_instance.get_all_user()
    return jsonify(data)


@app.route("/user/login", methods=['POST'])
def login():
    user_data = request.json
    message = firebase_service_instance.log_in(user_data)
    return jsonify(message)


@app.route("/user/reset", methods=['GET'])
def reset_password():
    user_data = request.json
    message = firebase_service_instance.reset_password(user_data)
    return jsonify(message)

@app.route("/user/ml/info", methods=['POST'])
def descobrir_tags_do_cliente():
    user_data = request.json

    tags_cabelo = user_data['categorias']
    for text in user_data['cabelo']:
        tags_cabelo.extend(ML.get_tags(text).split())

    tags_maquiagem = ML.get_tags(user_data['maquiagem']).split()
    tags_interesse = ML.get_tags(user_data['interesse']).split()
    
    data = firebase_service_instance_cliente.create_new_user({"email" : user_data['email'], 
                                                    "tags_cabelo" : tags_cabelo, 
                                                    "tags_interesse" : tags_interesse, 
                                                    "tags_maquiagem" : tags_maquiagem})

    return jsonify(data)
