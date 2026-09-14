import mysql.connector

class Database:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="ciel2027"
        )
        self.cursor = self.mydb.cursor()

    def getAllEtudiants(self):
        request_sql = "SELECT * FROM etudiant"
        self.cursor.execute(request_sql)
        result = self.cursor.fetchall()
        etudiants = []
        for row in result:
            etudiants.append({
                "idetudiant": row[0],
                "nom": row[1],
                "prenom": row[2],
                "email": row[3],
                "telephone": row[4]
            })
        return etudiants

    def getEtudiantById(self, id):
        req = f"SELECT * FROM etudiant WHERE idetudiant = {id}"
        self.cursor.execute(req)
        row = self.cursor.fetchone()
        if row is None:
            return None
        return {
            "idetudiant": row[0],
            "nom": row[1],
            "prenom": row[2],
            "email": row[3],
            "telephone": row[4]
        }

    def verifyUser(self, login, password):
        req = f"SELECT * FROM user WHERE login = '{login}' AND password = '{password}'"
        self.cursor.execute(req)
        user = self.cursor.fetchone()
        return user is not None