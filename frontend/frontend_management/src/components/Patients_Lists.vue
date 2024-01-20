<template>
    <div>
      <h1 class="title">Liste des Patients</h1>
  
      <!-- Barre de recherche, tri, et bouton Nouveau -->
      <div class="search-sort-container">
        <div class="controls-container">
          <button @click="addNewPatient" class="btn-new">Nouveau</button>
          <div class="sort-container">
            <label for="sortSelect">Trier par :</label>
            <select v-model="sortCriteria" id="sortSelect" @change="sortPatients" class="sort-select">
              <option value="name">Nom</option>
              <option value="gender">Sexe</option>
              <option value="createdAt">Date de création</option>
            </select>
          </div>
        </div>
        <div class="search-container">
          <input v-model="searchTerm" type="text" placeholder="Rechercher par nom" @input="filterPatients" class="search-input">
        </div>
      </div>
  
      <ul class="patient-list">
        <li v-for="patient in patients" :key="patient.id">
          <router-link :to="{ name: 'PatientsListe' }" class="patient-link">{{ patient.name }}</router-link>
        </li>
      </ul>
  
      <h2 class="dashboard-title">Liste des Patients</h2>
  
      <!-- Tableau de bord avec la barre de recherche -->
      <table class="patient-table">
        <thead>
          <tr>
            <th>Nom du patient</th>
            <th>Sexe</th>
            <th>Date de naissance</th>
            <th>Téléphone</th>
            <th>Adresse e-mail</th>
            <!-- Ajoutez d'autres en-têtes de colonnes selon vos besoins -->
          </tr>
        </thead>
        <tbody>
          <tr v-for="patient in sortedPatients" :key="patient.id">
            <td>
              <strong>{{ patient.name }}</strong><br>
            </td>
            <td>{{ patient.gender }}</td>
            <td>{{ patient.date_of_birth }}</td>
            <td>{{ patient.phone }}</td>
            <td>{{ patient.email }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        patients: [],
        searchTerm: '', // Variable pour stocker le terme de recherche
        sortCriteria: 'name', // Critère de tri par défaut
      };
    },
    computed: {
      // Utilisez une propriété calculée pour filtrer les patients en fonction de la recherche
      filteredPatients() {
        const term = this.searchTerm.toLowerCase();
        return this.patients.filter(patient => patient.name.toLowerCase().includes(term));
      },
      // Utilisez une propriété calculée pour trier les patients en fonction du critère de tri
      sortedPatients() {
        const criteria = this.sortCriteria;
        return this.patients.slice().sort((a, b) => {
          return a[criteria] < b[criteria] ? -1 : 1;
        });
      },
    },
    mounted() {
      console.log('Patients_Lists.vue is mounted');
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
      filterPatients() {
        // La recherche se met à jour automatiquement grâce à la propriété calculée
      },
      addNewPatient() {
        // Redirige vers la page d'ajout de patient
        this.$router.push({ name: 'AddPatient' });
      },
      sortPatients() {
        // La liste sera triée automatiquement grâce à la propriété calculée
      },
    },
  };
  </script>
  
  <style scoped>
  /* Styles spécifiques au composant (scoped) */
  
  .title {
    font-size: 24px;
    margin-bottom: 10px;
    color: #333;
  }
  
  .search-sort-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
  }
  
  .controls-container {
    display: flex;
    align-items: center;
  }
  
  .btn-new {
    padding: 8px 12px;
    font-size: 14px;
    background-color: #007bff;
    color: #fff;
    border: 1px solid #007bff;
    border-radius: 0 5px 5px 0;
    cursor: pointer;
  }
  
  .btn-new:hover {
    background-color: #0056b3;
  }
  
  .sort-container {
    margin-left: 10px;
  }
  
  .sort-select {
    padding: 8px;
    font-size: 14px;
  }
  
  .search-container {
    display: flex;
    align-items: center;
  }
  
  .search-input {
    flex: 1;
    padding: 8px;
    font-size: 14px;
    border: 1px solid #ddd;
    border-radius: 5px 0 0 5px;
  }
  
  .patient-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .patient-link {
    text-decoration: none;
    color: #007bff;
    font-weight: bold;
    margin-right: 10px;
  }
  
  .dashboard-title {
    font-size: 20px;
    margin-top: 20px;
    margin-bottom: 10px;
    color: #333;
  }
  
  .detail-label {
    font-weight: bold;
    margin-right: 5px;
  }
  
  .patient-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
  }
  
  .patient-table th, .patient-table td {
    border: 1px solid #ddd;
    padding: 10px;
    text-align: left;
  }
  
  .patient-table th {
    background-color: #f2f2f2;
  }
  </style>
  