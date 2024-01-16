# MedicTracker

MedicTracker est une application simple de suivi des patients développée avec Flask et MySQL.

## Configuration

### Prérequis

- Python 3.x
- MySQL Server

### Installation

1. Clonez le dépôt:

    ```bash
    git clone https://github.com/votre-utilisateur/MedicTracker.git
    ```

2. Accédez au répertoire du projet:

    ```bash
    cd MedicTracker
    ```

3. Installez les dépendances:

    ```bash
    pip install -r requirements.txt
    ```

4. Configurez la base de données MySQL:

    - Connectez-vous à MySQL:

        ```bash
        mysql -u root -p
        ```

    - Créez une base de données et un utilisateur:

        ```sql
        CREATE DATABASE medic_tracker;
        CREATE USER 'medic_user'@'localhost' IDENTIFIED BY 'your_password';
        GRANT ALL PRIVILEGES ON medic_tracker.* TO 'medic_user'@'localhost';
        FLUSH PRIVILEGES;
        ```

    Assurez-vous de remplacer `your_password` par un mot de passe sécurisé.

5. Initialisez la base de données:

    ```bash
    python init_db.py
    ```

## Utilisation

1. Exécutez l'application:

    ```bash
    python app.py
    ```

2. Ouvrez votre navigateur et accédez à [http://localhost:5000](http://localhost:5000).

3. Explorez les fonctionnalités pour ajouter, modifier et supprimer des patients.

## Contributions

Les contributions sont les bienvenues! N'hésitez pas à ouvrir une Pull Request.

## Licence

Ce projet est sous licence [MIT](LICENSE).

