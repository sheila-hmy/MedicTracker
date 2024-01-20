<template>
    <div>
      <h1 class="form-title">Ajouter un Patient</h1>
      <form @submit.prevent="addPatient" class="patient-form">
        <div class="form-group">
          <label for="patientName">Nom du Patient:</label>
          <input id="patientName" v-model="newPatient.name" required />
        </div>
  
        <div class="form-group">
          <label for="gender">Sexe:</label>
          <select id="gender" v-model="newPatient.gender" required>
            <option value="male">Masculin</option>
            <option value="female">Féminin</option>
            <!-- Ajoutez d'autres options selon vos besoins -->
          </select>
        </div>
  
        <div class="form-group">
          <label for="dateOfBirth">Date de Naissance:</label>
          <input id="dateOfBirth" type="date" v-model="newPatient.date_of_birth" required />
        </div>
  
        <div class="form-group">
          <label for="phone">Téléphone:</label>
          <input id="phone" v-model="newPatient.phone" required />
        </div>
  
        <div class="form-group">
          <label for="email">Adresse e-mail:</label>
          <input id="email" type="email" v-model="newPatient.email" required />
        </div>
  
        <!-- Ajoutez d'autres champs selon le besoin -->
  
        <div class="form-group">
          <button type="submit">Ajouter</button>
        </div>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        newPatient: {
          name: '',
          gender: 'male', // Valeur par défaut pour le sexe
          dateOfBirth: '',
          phone: '',
          email: '',
          // Ajoutez d'autres champs selon le besoin
        },
      };
    },
    methods: {
      addPatient() {
        axios
          .post('http://localhost:5000/patient', this.newPatient)
          .then((response) => {
            console.log(response.data.message);
            window.location.reload();
          })
          .catch((error) => {
            console.error("Une erreur s'est produite lors de l'ajout du patient", error);
          });
      },
    },
  };
  </script>
  
  <style scoped>
  .patient-form {
    max-width: 400px;
    margin: auto;
  }
  
  .form-group {
    margin-bottom: 20px;
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
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
  }
  
  button {
    background-color: #007bff;
    color: #fff;
    padding: 12px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  </style>
  