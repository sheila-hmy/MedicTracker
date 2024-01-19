from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_mysqldb import MySQL

app = Flask(__name__)
CORS(app, supports_credentials=True, origins="*")

app.secret_key = 'your_secret_key'

# Configuration de la base de données MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'medic_tracker'

# Initialisation de la connexion à la base de données
mysql = MySQL(app)

# Page d'affichage de la liste des patients
@app.route('/')
@cross_origin(supports_credentials=True)
def patients_list():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM patients")
    patients = cur.fetchall()
    cur.close()
    return jsonify(patients)

# Page d'enregistrement des patients (formulaire)
@app.route('/add_patient', methods=['POST'])
@cross_origin(supports_credentials=True)
def add_patient():
    data = request.get_json()
    name = data['name']
    gender = data['gender']
    date_of_birth = data['date_of_birth']
    patient_id = data['patient_id']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO patients (name, gender, date_of_birth, patient_id) VALUES (%s, %s, %s, %s)",
                (name, gender, date_of_birth, patient_id))
    mysql.connection.commit()
    cur.close()
    return jsonify(message='Patient enregistré avec succès')

# Page de modification des patients (formulaire)
@app.route('/edit_patient/<int:patient_id>', methods=['POST'])
@cross_origin(supports_credentials=True)
def edit_patient(patient_id):
    data = request.get_json()
    name = data['name']
    gender = data['gender']
    date_of_birth = data['date_of_birth']
    new_patient_id = data['patient_id']
    
    cur = mysql.connection.cursor()
    cur.execute("UPDATE patients SET name = %s, gender = %s, date_of_birth = %s, patient_id = %s WHERE id = %s",
                (name, gender, date_of_birth, new_patient_id, patient_id))
    mysql.connection.commit()
    cur.close()
    return jsonify(message='Patient modifié avec succès')

# Suppression d'un patient
@app.route('/delete_patient/<int:patient_id>', methods=['DELETE'])
@cross_origin(supports_credentials=True)
def delete_patient(patient_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM patients WHERE id = %s", (patient_id,))
    mysql.connection.commit()
    cur.close()
    return jsonify(message='Patient supprimé avec succès')

if __name__ == '__main__':
    app.run(debug=True)
