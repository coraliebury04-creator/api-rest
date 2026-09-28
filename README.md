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


## 🚀 Fonctionnalités & Évolution de l'API

### 🔹 Version 1 & 2 (`api_v1.py`, `api_v2.py`)
* Mise en place de la structure de base du serveur Flask.
* Connexion à la base de données MariaDB via le module `db.py`.

### 🔹 Version 3 (`api_v3.py`)
Implémentation complète des opérations **CRUD** sur les étudiants :
* `GET /v3/etudiants/` : Liste l'ensemble des étudiants.
* `GET /v3/etudiants/<id>` : Récupère les informations d'un étudiant spécifique.
* `POST /v3/etudiants/` : Ajoute un nouvel étudiant.
* `PUT /v3/etudiants/<id>` : Met à jour les données d'un étudiant.
* `DELETE /v3/etudiants/<id>` : Supprime un étudiant.

### 🔹 Version 4 (`api_v4.py`)
* Sécurisation des routes d'accès via `db.login(request)`.
* Gestion stricte des codes de statut HTTP (`200 OK`, `201 Created`, `401 Unauthorized`, `404 Not Found`, `500 Server Error`).

---

## ⚡ Installation et Lancement

### 1. Activer l'environnement virtuel
Dans le terminal PowerShell :
```powershell
.\venv\Scripts\Activate.ps1
