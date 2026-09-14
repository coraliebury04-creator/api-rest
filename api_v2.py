import pprint

from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Connexion à la BDD
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="ciel2027"
)

cursor = mydb.cursor()

# Route v2 pour récupérer tous les étudiants
@app.route('/v2/etudiants/', methods=['GET'])
def getEtudiants():
    etudiants = []
    request_sql = "SELECT * FROM etudiant"
    cursor.execute(request_sql)
    result = cursor.fetchall()
    
    for row in result:
        etudiant = {
            "idetudiant": row[0],
            "nom": row[1],
            "prenom": row[2],
            "email": row[3],
            "telephone": row[4]
        }
        etudiants.append(etudiant)
        
    return jsonify(etudiants), 200

# Route v2 avec gestion des erreurs (ID inexistant)
@app.route('/v2/etudiants/<int:id>', methods=['GET'])
def getEtudiant(id):
    req = f"SELECT * FROM etudiant WHERE idetudiant = {id}"
    pprint(req)
    cursor.execute(req)
    row = cursor.fetchone()
    
    # Vérification si l'étudiant existe en base
    if row is None:
        return jsonify({"erreur": "id invalide"}), 404
        
    etudiant = {
        "idetudiant": row[0],
        "nom": row[1],
        "prenom": row[2],
        "email": row[3],
        "telephone": row[4]
    }
    return jsonify(etudiant), 200

# Lancement
if __name__ == "__main__":
    app.run(debug=True)