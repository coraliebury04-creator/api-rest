from flask import Flask, jsonify, request
from db import Database

app = Flask(__name__)
db = Database()

@app.route('/v2/etudiants/', methods=['GET'])
def getEtudiants():
    etudiants = db.getAllEtudiants()
    return jsonify(etudiants), 200

@app.route('/v2/etudiants/<int:id>', methods=['GET'])
def getEtudiant(id):
    etudiant = db.getEtudiantById(id)
    if etudiant is None:
        return jsonify({"erreur": "id invalide"}), 404
    return jsonify(etudiant), 200


@app.route('/login/', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('login')
    pwd = data.get('password')

    if db.verifyUser(username, pwd):
        return jsonify({"message": "Connexion réussie"}), 200
    else:
        return jsonify({"erreur": "Identifiants incorrects"}), 401

if __name__ == "__main__":
    app.run(debug=True)