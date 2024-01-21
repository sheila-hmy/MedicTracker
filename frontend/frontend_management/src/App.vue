<template>
  <div id="app">
    <div v-if="$route.name !== 'add-patient'">
      <nav>
        <router-link to="/patients" class="btn-link">Liste des Patients</router-link> |
        <router-link to="/add-patient" class="btn-link">Ajouter un patient</router-link> |
        <router-link to="/edit-patient" class="btn-link">Modifier un patient</router-link> |
        <router-link to="/delete-patient" class="btn-link">Supprimer un patient</router-link>
      </nav>
    </div>
    <router-view />
  </div>
</template>

<script>
export default {
  methods: {
    logComponentDestroy() {
      console.log('Component destroyed:', this.$route.name);
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  padding: 30px;
}

nav {
  margin-bottom: 20px;
}

.btn-link {
  display: inline-block;
  padding: 10px;
  background-color: #1E3856;
  color: #fff;
  text-decoration: none;
  border-radius: 5px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  margin-right: 10px;
}

nav a.router-link-exact-active {
  color: #1E3856;
}
</style>
