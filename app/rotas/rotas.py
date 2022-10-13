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

@app.route("/cliente", methods=['POST'])
def get_cliente():
    user_data = request.json
    data = firebase_service_instance_cliente.get_user_by_email(user_data)
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

@app.route("/user/ml/infocliente", methods=['POST'])
def descobrir_tags_do_cliente():
    user_data = request.json

    tags_cabelo = user_data['categorias']
    for text in user_data['cabelo']:
        tags_cabelo.extend(ML.get_tags(text).split())

    tags_maquiagem = ML.get_tags(user_data['maquiagem']).split()
    tags_interesse = ML.get_tags(user_data['interesse']).split()

    tags = []
    tags.extend([x for x in tags_maquiagem])
    tags.extend([x for x in tags_cabelo])
    tags.extend([x for x in tags_interesse])

    data = firebase_service_instance_cliente.create_new_user({"email" : user_data['email'], "tags" : tags})

    return jsonify(data)


@app.route("/user/ml/infoprestador", methods=['POST'])
def descobrir_tags_do_prestador():
    user_data = request.json
    tags_descricao = user_data['categorias']
    tags_descricao.extend(ML.get_tags(user_data['descricao']).split())
    data = firebase_service_instance_prestador.create_new_user({"email" : user_data['email'], "tags" : tags_descricao})

    return jsonify(data)


@app.route("/user/ml/recomendacao", methods=['POST'])
def get_recomendacao():
    user_data = request.json
    cliente = firebase_service_instance_cliente.get_user_by_email(user_data)
    prestadores = firebase_service_instance_prestador.get_all_user()

    recomendados = []
    pontuacao = {}
    for prestador in prestadores['data']:
        pontos = 0
        for tagc in cliente['data']['tags']:
            if tagc in prestador['tags']:
                pontos += 1
        pontuacao[prestador['email']] = pontos

    for email in sorted(pontuacao, reverse=True, key=pontuacao.get):
        recomendados.extend([prestador for prestador in prestadores['data'] if prestador['email'] == email])

    return jsonify(recomendados)