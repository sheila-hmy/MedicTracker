<!-- src/views/EditPatient.vue -->
<template>
    <div>
      <h1>Modifier un Patient</h1>
      <select v-model="selectedPatient" @change="fetchPatientDetails">
        <option v-for="patient in patients" :key="patient.id" :value="patient.id">{{ patient.name }}</option>
      </select>
      <form @submit.prevent="updatePatient">
        <label>Nom du Patient:</label>
        <input v-model="patientDetails.name" required />
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
        }
      },
      updatePatient() {
        axios.put(`http://localhost:5000/patients/${this.selectedPatient}`, this.patientDetails)
          .then(response => {
            console.log(response.data.message);
            this.$router.push({ name: 'PatientList' }); // Rediriger vers la liste des patients après la modification
          })
          .catch(error => {
            console.error('Une erreur s\'est produite lors de la modification du patient', error);
          });
      },
    },
  };
  </script>
  