// router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import PatientsList from '../components/Patients_Lists.vue';
import AddPatient from '../components/AddPatient.vue';
import EditPatient from '../components/EditPatient.vue';
import DeletePatient from '../components/DeletePatient.vue';

const routes = [
  { path: '/patients', name: 'PatientsListe', component: PatientsList },
  { path: '/add-patient', name: 'AddPatient', component: AddPatient },
  { path: '/edit-patient', name: 'EditPatient', component: EditPatient },
  { path: '/delete-patient', name: 'DeletePatient', component: DeletePatient },
  // ... autres routes
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
