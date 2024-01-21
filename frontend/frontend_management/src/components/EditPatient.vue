<!-- src/views/EditPatient.vue -->
<template>
  <div class="edit-patient-container">
    <h1 class="form-title">Modifier un Patient</h1>
    <div class="select-container">
      <select v-model="selectedPatient" @change="fetchPatientDetails">
        <option v-for="patient in patients" :key="patient.id" :value="patient.id">{{ patient.id }}</option>
      </select>
    </div>
    <form @submit.prevent="updatePatient" class="patient-form">
      <div class="form-group">
        <label for="name">Nom du Patient:</label>
        <input id="name" v-model="patientDetails.name" required />
      </div>
      <div class="form-group">
        <label for="gender">Genre:</label>
        <select id="gender" v-model="patientDetails.gender" required>
          <option value="male">Masculin</option>
          <option value="female">Féminin</option>
        </select>
      </div>
      <div class="form-group">
        <label for="dateOfBirth">Date de naissance:</label>
        <input id="dateOfBirth" type="date" v-model="patientDetails.date_of_birth" required />
      </div>
      <div class="form-group">
        <label for="phone">Téléphone:</label>
        <input id="phone" v-model="patientDetails.phone" required />
      </div>
      <div class="form-group">
        <label for="email">Adresse e-mail:</label>
        <input id="email" type="email" v-model="patientDetails.email" required />
      </div>
      <button type="submit">Enregistrer</button>
    </form>
  </div>
</template>

<style scoped>
.edit-patient-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

h1 {
  font-size: 20px;
  margin-bottom: 15px;
}

.select-container {
  margin-bottom: 15px;
}

.patient-form {
  display: grid;
  gap: 10px;
}

.form-group {
  display: grid;
  gap: 5px;
}

label {
  display: block;
    margin-bottom: 8px;
    font-weight: bold;
    color: #333;
}

input,
select {
  width: 100%;
  padding: 8px;
  font-size: 14px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  background-color: #1E3856;
  color: #fff;
  padding: 8px 14px;
  border: none;
  cursor: pointer;
  font-size: 14px;
}

button:hover {
  background-color: #2980b9;
}
</style>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      patients: [],
      selectedPatient: null,
      patientDetails: {
        name: '',
        gender: '',
        date_of_birth: '',
        phone: '',
        email: '',
      },
    };
  },
  mounted() {
    this.fetchPatients();
  },
  methods: {
    fetchPatients() {
      axios.get('http://localhost:5000/patients')
        .then(response => {
          this.patients = response.data;
        })
        .catch(error => {
          console.error('Une erreur s\'est produite lors de la récupération des patients', error);
        });
    },
    fetchPatientDetails() {
      const selectedPatientId = parseInt(this.selectedPatient);
      const selectedPatient = this.patients.find(patient => patient.id === selectedPatientId);

      if (selectedPatient) {
        this.patientDetails = { ...selectedPatient };
        this.patientDetails.date_of_birth = new Date(selectedPatient.date_of_birth).toISOString().split('T')[0];
      }
    },
    updatePatient() {
      axios.put(`http://localhost:5000/update/${this.selectedPatient}`, this.patientDetails)
        .then(response => {
          console.log(response.data.message);
          window.location.reload();
        })
        .catch(error => {
          console.error('Une erreur s\'est produite lors de la modification du patient', error);
        });
    },
  },
};
</script>
