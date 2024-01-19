<template>
  <div class="main-content">
    <div class="content-section">
      <!-- Contenu spécifique pour chaque section comme Facturation, Patients, etc. -->
      <DashboardComponent />
      <!-- Vous pouvez ajouter d'autres sous-composants ici -->
    </div>
  </div>
</template>

<script>
import DashboardComponent from './DashboardComponent.vue';

export default {
  components: {
    DashboardComponent
  }
}
</script>

<style scoped>
.main-content {
  flex-grow: 1;
  padding: 20px;
}
</style>