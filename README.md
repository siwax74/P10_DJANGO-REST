# 🌐 ***DJANGO_REST - SOFTDESK*** 🌐
# **Application Support**

## 📋 Fonctionnalités

1. Gestion des utilisateurs : Inscription, connexion, confidentialité (RGPD), token JWT.
2. Gestion des projets : Création, attribution de contributeurs, accès restreint.
3. Gestion des tâches (Issues) : Création, priorisation (LOW, MEDIUM, HIGH), suivi (To Do, WIP, Done).
4. Gestion des commentaires : Ajout et suivi des discussions sur les issues.

## 📂 Installation

Pour installer SofDesk, suivez ces étapes :

1. Vérifiez que Python 3.8 ou une version supérieure est installé sur votre machine.
    Exécutez la commande suivante dans votre terminal pour vérifier la version installée :
    ```bash
    Copier le code
    python --version
    ```
    ou, selon votre configuration :
    ```bash
    Copier le code
    python3 --version
    ```
    Si la version affichée est inférieure à 3.8 ou si Python n'est pas installé, téléchargez et installez une version récente depuis le site officiel.
    ```bash
    https://www.python.org/downloads/
   ```
2. Clonez le dépôt Git :
   ```bash
   git clone https://github.com/siwax74/P10_DJANGO_REST
   ```
3. Créer l'environnement virtuel :
   ```bash
   python -m venv env
   ```
4. Activez l'environnement virtuel :
   ```bash
   source env/bin/activate # Sur Mac/Linux
   env\Scripts\activate    # Sur Windows
   ```
5. Installez les dépendances nécessaires :
   ```bash
   pip install -r requirements.txt
   ```
6. Démarrez le serveur de développement :
   ```bash
   python manage.py runserver
   ```

## 🚀 Utilisation

1. **Accédez à l'application dans votre navigateur** :
   [http://localhost:8000](http://localhost:8000)

2. **Créer un compte utilisateur** :
   - [http://localhost:8000/api/auth/login/](http://localhost:8000/api/auth/signup/)

3. **Se connecter** :
   - [http://localhost:8000/api/auth/login/](http://localhost:8000/api/auth/login/)

## Comptes de test

- **Compte 1**:
  - Email : `test1@gmail.com`
  - Mot de passe : `test1`

- **Compte 2**:
  - Email : `test2@gmail.com`
  - Mot de passe : `test2`
 
- **Compte 3**:
  - Email : `test3@gmail.com`
  - Mot de passe : `test3`

## 🛠 **Maintenance et Améliorations Futures**
Voici quelques améliorations prévues pour les versions futures :
- Validation Email
- Sécurité
- Performance
- Expérience Dev
- Expérience utilisateur

## 👨‍💻 Auteur

- **DG.**

## 📄 Licence

Ce projet est sous licence MIT. Vous êtes libre de modifier et de redistribuer le code source. Consultez le fichier `LICENSE` pour plus d'informations.

## Remerciements

Un grand merci aux contributeurs de Django et de toutes les bibliothèques utilisées dans ce projet pour leur travail incroyable !
Merci également à l'organisme de formation OpenClassrooms pour son soutien pédagogique.
