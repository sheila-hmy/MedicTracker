<template>
    <div>
      <HeaderComponent />
      <div class="container">
        <SidebarComponent />
        <MainContentComponent />
      </div>
    </div>
  </template>
  
  <script>
  import HeaderComponent from './HeaderComponent.vue';
  import SidebarComponent from './SidebarComponent.vue';
  import MainContentComponent from './MainContentComponent.vue';
  
  export default {
    components: {
      HeaderComponent,
      SidebarComponent,
      MainContentComponent
    }
  }
  </script>
  
  <style scoped>
  .container {
    display: flex;
  }
  </style>