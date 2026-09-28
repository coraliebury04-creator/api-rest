# API REST - Gestion des Étudiants (BTS CIEL)

Ce projet met en œuvre un service web API REST avec Flask et MySQL pour la gestion de la base de données `ciel2027`.

---

## 🛠️ Stack Technique

* **Langage :** Python 3.14
* **Framework Web :** Flask
* **Base de données :** MySQL / MariaDB (`ciel2027`)
* **Connecteur BDD :** `mysql-connector-python`
* **Environnement virtuel :** `venv`

---

## 📂 Structure du Projet

```text
api-rest/
├── api_v1.py        # Version 1 : API basique
├── api_v2.py        # Version 2 : Intégration de la classe Database
├── api_v3.py        # Version 3 : Gestion complète CRUD des étudiants
├── api_v4.py        # Version 4 : Sécurisation et authentification (Basic Auth)
├── db.py            # Classe de connexion et requêtes vers la base de données
├── ciel2027.sql     # Script d'initialisation de la base de données
└── README.md        # Documentation et rapport du projet
