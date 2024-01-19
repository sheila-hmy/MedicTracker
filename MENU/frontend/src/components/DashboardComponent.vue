<template>
  <div class="dashboard">
    <div class="dashboard-item">
      <img src="../assets/hopital.jpg" alt="Hopital Image" />
    </div>
    <!-- Ajoutez d'autres items de tableau de bord ici -->
  </div>
</template>

<style scoped>
html, body {
  height: 100%;
  margin: 0;
  padding: 0;
}

.dashboard {
  display: flex;
  flex-direction: column;
  height: 100%; /* Assurez-vous que le conteneur occupe toute la hauteur du body */
}

.dashboard-item {
  /* Styles pour vos items de tableau de bord */
  flex: 1; /* Faites en sorte que le conteneur occupe tout l'espace disponible */
  color: white; /* Ajoutez une couleur de texte appropriée */
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden; /* Cache le dépassement d'image pour éviter les problèmes de distorsion */
}

.dashboard-item img {
  width: 100%;
  height: 100%;
  object-fit: cover; /* Ajustez la taille de l'image pour couvrir toute la zone */
  margin: 0; /* Réinitialise les marges par défaut */
  padding: 0; /* Réinitialise les paddings par défaut */
}
</style>
