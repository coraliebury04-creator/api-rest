import mysql.connector
from flask import Flask, jsonify, request

app = Flask(__name__)


mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="ciel2027"
)
cursor = mydb.cursor()


def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return False

    username = auth.username
    password = auth.password

    req = f"SELECT * FROM user WHERE login = '{username}' AND password = '{password}'"
    cursor.execute(req)
    data = cursor.fetchone()

    if data:
        return True
    else:
        return False



@app.route('/v3/etudiants', methods=['GET', 'POST'])
def handleEtudiants():
    if not login():
        return jsonify("Accès refusé"), 401

    if request.method == 'POST':
        data = request.get_json() or {}
        nom = data.get('nom', '')
        prenom = data.get('prenom', '')
        email = data.get('email', '')
        telephone = data.get('telephone', '')

        req = f"INSERT INTO etudiant (nom, prenom, email, telephone) VALUES ('{nom}', '{prenom}', '{email}', '{telephone}')"
        cursor.execute(req)
        mydb.commit()

        return jsonify({'message': 'Étudiant créé'}), 201

    # Cas du GET
    etudiants = []
    req = "SELECT * FROM etudiant"
    cursor.execute(req)
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

@app.route('/v3/etudiants/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handleEtudiantById(id):
    if not login():
        return jsonify("Accès refusé"), 401

    if request.method == 'GET':
        req = f"SELECT * FROM etudiant WHERE idetudiant = {id}"
        cursor.execute(req)
        row = cursor.fetchone()
        if row:
            etudiant = {
                "idetudiant": row[0],
                "nom": row[1],
                "prenom": row[2],
                "email": row[3],
                "telephone": row[4]
            }
            return jsonify(etudiant), 200
        else:
            return jsonify({"erreur": "Étudiant non trouvé"}), 404

    elif request.method == 'PUT':
        data = request.get_json() or {}
        nom = data.get('nom', '')
        prenom = data.get('prenom', '')
        email = data.get('email', '')
        telephone = data.get('telephone', '')

        req = f"UPDATE etudiant SET nom='{nom}', prenom='{prenom}', email='{email}', telephone='{telephone}' WHERE idetudiant={id}"
        cursor.execute(req)
        mydb.commit()

        return jsonify({'message': 'Modification OK'}), 200

    elif request.method == 'DELETE':
        req = f"DELETE FROM etudiant WHERE idetudiant={id}"
        cursor.execute(req)
        mydb.commit()

        return jsonify({'message': 'Suppression OK'}), 200

if __name__ == "__main__":
    app.run(debug=True)