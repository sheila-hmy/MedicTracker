from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configuration de la base de données MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Utilisez le nom d'utilisateur MySQL que vous avez configuré
app.config['MYSQL_PASSWORD'] = '123456'  # Utilisez le mot de passe MySQL que vous avez configuré
app.config['MYSQL_DB'] = 'medic_tracker'  # Utilisez le nom de la base de données MySQL que vous avez créé

# Initialisation de la connexion à la base de données
mysql = MySQL(app)

# Page d'affichage de la liste des patients
@app.route('/')
def patients_list():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM patients")
    patients = cur.fetchall()
    cur.close()
    return render_template('patients_list.html', patients=patients)

# Page d'enregistrement des patients (formulaire)
@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        date_of_birth = request.form['date_of_birth']
        patient_id = request.form['patient_id']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO patients (name, gender, date_of_birth, patient_id) VALUES (%s, %s, %s, %s)",
                    (name, gender, date_of_birth, patient_id))
        mysql.connection.commit()
        cur.close()
        flash('Patient enregistré avec succès', 'success')
        return redirect(url_for('patients_list'))
    return render_template('add_patient.html')

# Page de modification des patients (formulaire)
@app.route('/edit_patient/<int:patient_id>', methods=['GET', 'POST'])
def edit_patient(patient_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM patients WHERE id = %s", (patient_id,))
    patient = cur.fetchone()
    cur.close()

    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        date_of_birth = request.form['date_of_birth']
        new_patient_id = request.form['patient_id']
        
        cur = mysql.connection.cursor()
        cur.execute("UPDATE patients SET name = %s, gender = %s, date_of_birth = %s, patient_id = %s WHERE id = %s",
                    (name, gender, date_of_birth, new_patient_id, patient_id))
        mysql.connection.commit()
        cur.close()
        flash('Patient modifié avec succès', 'success')
        return redirect(url_for('patients_list'))

    return render_template('edit_patient.html', patient=patient)

# Suppression d'un patient
@app.route('/delete_patient/<int:patient_id>', methods=['POST'])
def delete_patient(patient_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM patients WHERE id = %s", (patient_id,))
    mysql.connection.commit()
    cur.close()
    flash('Patient supprimé avec succès', 'success')
    return redirect(url_for('patients_list'))

if __name__ == '__main__':
    app.run(debug=True)
