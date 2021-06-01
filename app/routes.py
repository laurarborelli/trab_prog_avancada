from flask import json, request, jsonify
import flask
from bson import json_util
from app import app
from app import db
from bson.objectid import ObjectId

@app.route('/')
@app.route('/index')
def index():
    return flask.jsonify(json.loads(json_util.dumps(db.lanches.find({}).sort("_id", 1))))

@app.route('/criar', methods=['POST'])
def create():
    json_data = request.json
    if json_data is not None:
        db.lanches.insert_one(json_data)
        return jsonify(mensagem='lanches criados')
    else:
        return jsonify(mensagem='lanches não criado')
@app.route("/getid/<string:lanchesId>")
def getid(lanchesId):
    lanches = db.lanches.find_one({"_id": ObjectId(lanchesId
)})
    return flask.jsonify(json.loads(json_util.dumps(lanches)))

@app.route("/delete/<string:lanchesId>")
def delete(lanchesId):
    result = db.lanches.delete_one({"_id": ObjectId(lanchesId)})
    if(result.deleted_count > 0):
        return jsonify(mensagem='lanches removido')
    else:
        return jsonify(mensagem='lanches não removido')

@app.route('/update', methods=['POST'])
def update():
    json_data = request.json
    if json_data is not None and db.lanches.find_one({"_id": ObjectId(json_data["id"])}) is not None:
        db.lanches.update_one({'_id': ObjectId(json_data["id"])}, {"$set": {'nome': json_data["nome"], 'preco': json_data["preco"],'pao': json_data["pao"], 'hamburguer': json_data["hamburguer"], 'salada': json_data["salada"], 'cebola': json_data["cebola"], 'queijo': json_data["queijo"], 'batatinha': json_data["batatinha"], 'selected': json_data["selected"]}})
        return jsonify(mensagem='lanches atualizado')
    else:
        return jsonify(mensagem='lanches não atualizado')
