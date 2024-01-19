<template>
  <header class="header">
    <div class="logo">
      <img src="../assets/Logo Hannah.jpg" alt="Logo" class="logo-image" />
      <div class="header-title">CLINIQUE HANNAH</div>
    </div>
    <!-- Autres éléments de l'en-tête ici, si nécessaire -->
  </header>
</template>
  
  <script>
  export default {
    name: 'HeaderComponent'
  }
  </script>
  
  <style scoped>
  .header {
    background-color: #34495E;
    padding: 10px;
    color: white;
    text-align: center;
  }
  .header-title {
    font-size: 24px;
    font-weight: bold;
  }
  .logo {
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .logo-image {
    width: 50px;
    height: 50px;
    margin-right: 10px;
    }
</style>