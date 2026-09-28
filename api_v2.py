from flask import Flask, jsonify, request
from db import Database, Etudiant

app = Flask(__name__)
app.url_map.strict_slashes = False

db = Database()

@app.route('/v2/etudiants', methods=['GET'])
def getEtudiants():
    etudiants = db.getAllEtudiants()
    etudiants_dict = [e.__dict__ for e in etudiants]
    return jsonify(etudiants_dict), 200

@app.route('/v2/etudiants/<int:id>', methods=['GET'])
def getEtudiant(id):
    etudiant = db.getEtudiantById(id)
    if etudiant is None:
        return jsonify({"erreur": "id invalide"}), 404
    return jsonify(etudiant.__dict__), 200

@app.route('/v2/etudiants', methods=['POST'])
def createEtudiant():
    data = request.get_json()
    if not data:
        return jsonify({"erreur": "Données manquantes ou format non valide"}), 400

    nouveau = Etudiant(
        nom=data.get('nom'),
        prenom=data.get('prenom'),
        email=data.get('email'),
        telephone=data.get('telephone')
    )
    
    if hasattr(db, 'addEtudiant'):
        db.addEtudiant(nouveau)
    elif hasattr(db, 'saveEtudiant'):
        db.saveEtudiant(nouveau)
    elif hasattr(db, 'insertEtudiant'):
        db.insertEtudiant(nouveau)

    return jsonify({"message": "Étudiant créé avec succès"}), 201

@app.route('/v2/etudiants/<int:id>', methods=['PUT'])
def updateEtudiant(id):
    data = request.get_json()
    if not data:
        return jsonify({"erreur": "Données manquantes"}), 400

    etudiant = db.getEtudiantById(id)
    if etudiant is None:
        return jsonify({"erreur": "Étudiant non trouvé"}), 404

    if hasattr(db, 'updateEtudiant'):
        db.updateEtudiant(id, data)

    return jsonify({"message": "Étudiant mis à jour avec succès"}), 200

@app.route('/v2/etudiants/<int:id>', methods=['DELETE'])
def deleteEtudiant(id):
    etudiant = db.getEtudiantById(id)
    if etudiant is None:
        return jsonify({"erreur": "Étudiant non trouvé"}), 404

    if hasattr(db, 'deleteEtudiant'):
        db.deleteEtudiant(id)

    return jsonify({"message": "Étudiant supprimé avec succès"}), 200

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"erreur": "Données manquantes"}), 400

    username = data.get('login')
    pwd = data.get('password')

    if db.verifyUser(username, pwd):
        return jsonify({"message": "Connexion réussie"}), 200
    else:
        return jsonify({"erreur": "Identifiants incorrects"}), 401

if __name__ == "__main__":
    app.run(debug=True)