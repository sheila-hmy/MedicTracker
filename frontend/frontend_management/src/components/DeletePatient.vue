<!-- src/views/DeletePatient.vue -->
<template>
    <div>
      <h1>Supprimer un Patient</h1>
      <select v-model="selectedPatient">
        <option v-for="patient in patients" :key="patient.id" :value="patient.id">{{ patient.name }}</option>
      </select>
      <button @click="deletePatient">Supprimer</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        patients: [],
        selectedPatient: null,
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
      deletePatient() {
        const confirmed = window.confirm('Êtes-vous sûr de vouloir supprimer ce patient?');
  
        if (confirmed) {
          axios.delete(`http://localhost:5000/delete/${this.selectedPatient}`)
            .then(response => {
              console.log(response.data.message);
              window.location.reload();
            })
            .catch(error => {
              console.error('Une erreur s\'est produite lors de la suppression du patient', error);
            });
        }
      },
    },
  };
  </script>
  