<!-- src/views/DeletePatient.vue -->
<template>
  <div class="delete-patient-container">
    <h1>Supprimer un Patient</h1>
    <div class="select-container">
      <select v-model="selectedPatient">
        <option v-for="patient in patients" :key="patient.id" :value="patient.id">{{ patient.name }}</option>
      </select>
    </div>
    <button @click="deletePatient">Supprimer</button>
  </div>
</template>

<style scoped>
.delete-patient-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

h1 {
  font-size: 24px;
  margin-bottom: 20px;
}

.select-container {
  margin-bottom: 20px;
}

select {
  width: 100%;
  padding: 8px;
  font-size: 16px;
}

button {
  background-color: #1E3856;
  color: #fff;
  padding: 10px 20px;
  border: none;
  cursor: pointer;
  font-size: 16px;
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
