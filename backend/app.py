from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Pour mysql

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/db_name'

db = SQLAlchemy(app)
CORS(app)  # Permet les requêtes CORS

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()

@app.route('/patient', methods=['POST'])
def add_patient():
    data = request.json

    new_patient = Patient(
        name=data['name'],
        gender=data['gender'],
        date_of_birth=datetime.strptime(data['date_of_birth'], '%Y-%m-%d').date(),
        phone=data['phone'],
        email=data['email']
    )


    try:
        db.session.add(new_patient)
        db.session.commit()
        print("bien")
        return jsonify({'message': 'Patient ajouté avec succès'}), 201
    except Exception as e:
        db.session.rollback()
        print(str(e))
        return jsonify({'error': f"Une erreur s'est produite lors de l'ajout du patient: {str(e)}"}), 500


@app.route('/patients', methods=['GET'])
def get_patients():
    patients = Patient.query.all()
    patients_list = [patient.as_dict() for patient in patients]
    return jsonify(patients_list)

@app.route('/delete/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    print(patient)

    try:
        db.session.delete(patient)
        print(" deleted")
        db.session.commit()
        return jsonify({'message': 'Patient supprimé avec succès'}), 200
    except Exception as e:
        db.session.rollback()
        print(str(e))
        return jsonify({'error': f'Une erreur s\'est produite lors de la suppression du patient: {str(e)}'}), 500


@app.route('/update/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id):
    data = request.get_json()
    patient = Patient.query.get_or_404(patient_id)

    patient.name = data['name']
    patient.gender = data['gender']
    patient.date_of_birth = datetime.strptime(data['date_of_birth'], '%Y-%m-%d').date()
    patient.phone = data['phone']
    patient.email = data['email']

    try:
        db.session.commit()
        print("patient updated")
        return jsonify({'message': 'Patient modifié avec succès'})
    except Exception as e:
        db.session.rollback()
        print(str(e))
        return jsonify({'error': f'Une erreur s\'est produite lors de la modification du patient: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
