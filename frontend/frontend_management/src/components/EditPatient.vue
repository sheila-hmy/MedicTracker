<!-- src/views/EditPatient.vue -->
<template>
    <div>
      <h1>Modifier un Patient</h1>
      <select v-model="selectedPatient" @change="fetchPatientDetails">
        <option v-for="patient in patients" :key="patient.id" :value="patient.id">{{ patient.id }}</option>
      </select>
      <form @submit.prevent="updatePatient">
        <label>Nom du Patient:</label>
        <input v-model="patientDetails.name" required />
        <select id="gender" v-model="patientDetails.gender" required>
            <option value="male">Masculin</option>
            <option value="female">Féminin</option>
            <!-- Ajoutez d'autres options selon vos besoins -->
          </select>
        <div class="form-group">
        <label>Date de naissance:</label>
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
        <!-- Ajoutez d'autres champs selon le formulaire -->
        <button type="submit">Enregistrer les modifications</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        patients: [],
        selectedPatient: null,
        patientDetails: {
          name: '',
          // Ajoutez d'autres champs selon le formulaire
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
        // Charger les détails du patient sélectionné pour pré-remplir le formulaire
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
  