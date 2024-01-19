<!-- <template>
  <div class="sidebar">
    <div class="sidebar-header">
      CLINIQUE HANNAH
    </div>
    <div class="menu-item" @click="toggleSubMenu(0)">
      Accueil
      <div class="sub-menu" :class="{ show: activeSubMenuIndex === 0 }">
        <div class="sub-menu-item">Sous-tâche 1</div>
        <div class="sub-menu-item">Sous-tâche 2</div>
      </div>
    </div>
    <div class="menu-item" @click="toggleSubMenu(1)">
      Patient
      <div class="sub-menu" :class="{ show: activeSubMenuIndex === 1 }">
        <div class="sub-menu-item">Sous-tâche 1</div>
        <div class="sub-menu-item">Sous-tâche 2</div>
      </div>
    </div>
    <div class="menu-item" @click="toggleSubMenu(2)">
      Consultation
      <div class="sub-menu" :class="{ show: activeSubMenuIndex === 2 }">
        <div class="sub-menu-item">Sous-tâche 1</div>
        <div class="sub-menu-item">Sous-tâche 2</div>
      </div>
    </div>
    <div class="menu-item" @click="toggleSubMenu(2)">
      Document
      <div class="sub-menu" :class="{ show: activeSubMenuIndex === 2 }">
        <div class="sub-menu-item">Sous-tâche 1</div>
        <div class="sub-menu-item">Sous-tâche 2</div>
      </div>
    </div>
    <div class="menu-item" @click="toggleSubMenu(2)">
      Planning
      <div class="sub-menu" :class="{ show: activeSubMenuIndex === 2 }">
        <div class="sub-menu-item">Sous-tâche 1</div>
        <div class="sub-menu-item">Sous-tâche 2</div>
      </div>
    </div>
    <div class="menu-item" @click="toggleSubMenu(2)">
      Facturation 
      <div class="sub-menu" :class="{ show: activeSubMenuIndex === 2 }">
        <div class="sub-menu-item">Sous-tâche 1</div>
        <div class="sub-menu-item">Sous-tâche 2</div>
      </div>
    </div>
    <div class="menu-item" @click="toggleSubMenu(2)">
      Honoraire des Gardes
      <div class="sub-menu" :class="{ show: activeSubMenuIndex === 2 }">
        <div class="sub-menu-item">Sous-tâche 1</div>
        <div class="sub-menu-item">Sous-tâche 2</div>
      </div>
    </div>
    <div class="menu-item" @click="toggleSubMenu(2)">
      Honoraires par taux
      <div class="sub-menu" :class="{ show: activeSubMenuIndex === 2 }">
        <div class="sub-menu-item">Sous-tâche 1</div>
        <div class="sub-menu-item">Sous-tâche 2</div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.sidebar {
  background-color: #1E3856;
  color: white;
  width: 250px;
  height: calc(100vh - 20px);
  display: flex;
  flex-direction: column;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.sidebar-header {
  background-color: #0F2340;
  padding: 20px;
  font-size: 24px;
  text-align: center;
  border-bottom: 1px solid #4F7A9C;
  font-weight: 600;
}

.menu-item {
  position: relative;
  cursor: pointer;
  margin-bottom: 10px; /* Ajout de marge inférieure pour espacement */
}

.sub-menu {
  display: none;
}

.sub-menu.show {
  display: block;
}

.sub-menu-item {
  padding: 10px 20px;
  font-size: 16px;
  border-bottom: 1px solid #4F7A9C;
  transition: background-color 0.3s ease;
}

.sub-menu-item:last-child {
  border-bottom: none;
}

.sub-menu-item:hover {
  background-color: #144C73;
}
</style>

<script>
export default {
  data() {
    return {
      activeSubMenuIndex: -1
    };
  },
  methods: {
    toggleSubMenu(index) {
      this.activeSubMenuIndex = this.activeSubMenuIndex === index ? -1 : index;
    }
  }
};
</script> -->

<!-- <template>
  <div class="sidebar">
    <div class="sidebar-header">
      <span>MENU</span>
      CLINIQUE HANNAH
    </div>
    <div v-for="(menuItem, index) in menuItems" :key="index" class="menu-item" @click="toggleSubMenu(index)">
      <FontAwesomeIcon :icon="menuItem.icon" /> {{ menuItem.label }}
      <div class="sub-menu" :class="{ show: activeSubMenuIndex === index }">
        <div v-for="(subItem, subIndex) in menuItem.subMenu" :key="subIndex" class="sub-menu-item">
          {{ subItem }}
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.sidebar {
  background-color: #1E3856;
  color: white;
  width: 250px;
  height: calc(100vh - 20px);
  display: flex;
  flex-direction: column;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  box-shadow: 2px 0px 5px rgba(0, 0, 0, 0.2); /* Ajout d'une légère ombre à la barre latérale */
}

.sidebar-header {
  background-color: #0F2340;
  padding: 10px;
  font-size: 17px;
  text-align: center;
  border-bottom: 1px solid #4F7A9C;
  font-weight: 600;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 23px; 
}

.sidebar-header span {
  font-size: 16px;
  margin-bottom: 5px;
}

.menu-item {
  position: relative;
  cursor: pointer;
  margin-bottom: 60px;
  font-size: 21px;
  margin-left: 12px
}

.sub-menu {
  display: none;
}

.sub-menu.show {
  display: block;
}

.sub-menu-item {
  padding: 10px 20px;
  font-size: 16px;
  border-bottom: 1px solid #4F7A9C;
  transition: background-color 0.3s ease;
}

.sub-menu-item:last-child {
  border-bottom: none;
}

.sub-menu-item:hover {
  background-color: #144C73;
}
</style>

<script>
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faHome, faUser, faSearch, faFile, faCalendar, faMoneyBill, faClock, faPercent,} from '@fortawesome/free-solid-svg-icons';
library.add(faHome, faUser, faSearch, faFile, faCalendar, faMoneyBill, faClock, faPercent,);

export default {
  components: {
    FontAwesomeIcon,
  },
  data() {
    return {
      activeSubMenuIndex: -1,
      menuItems: [
        { label: "Accueil", subMenu: ["Sous-tâche 1", "Sous-tâche 2"], icon: ['fas', 'home'] },
        { label: "Patient", subMenu: ["Sous-tâche 1", "Sous-tâche 2"], icon: ['fas', 'user'] },
        { label: "Consultation", subMenu: ["Sous-tâche 1", "Sous-tâche 2"], icon: ['fas', 'search']},
        { label: "Documents", subMenu: ["Sous-tâche 1", "Sous-tâche 2"], icon: ['fas', 'file']},
        { label: "Planning", subMenu: ["Sous-tâche 1", "Sous-tâche 2"], icon: ['fas', 'calendar'] },
        { label: "Facturation", subMenu: ["Sous-tâche 1", "Sous-tâche 2"], icon: ['fas', 'money-bill'] },
        { label: "Honoraire des Gardes", subMenu: ["Sous-tâche 1", "Sous-tâche 2"], icon: ['fas', 'clock'] },
        { label: "Honoraires par taux", subMenu: ["Sous-tâche 1", "Sous-tâche 2"], icon: ['fas', 'percent'] },
        // Ajoutez le reste des éléments de menu ici
      ]
    };
  },
  methods: {
    toggleSubMenu(index) {
      this.activeSubMenuIndex = this.activeSubMenuIndex === index ? -1 : index;
    }
  }
};
</script> -->

<!-- <template>
  <div class="sidebar">
    <div class="sidebar-header">
      <div class="logo-container">
        <img src="../assets/Logo Hannah.jpg" alt="Logo de clinique" class="logo" />
        <span>CLINIQUE HANNAH</span>
      </div>
      <span>MENU</span>
    </div>
    <div v-for="(menuItem, index) in menuItems" :key="index">
      <div class="menu-item" @click="toggleSubMenu(index)">
        <FontAwesomeIcon :icon="menuItem.icon" class="icon" />
        {{ menuItem.label }}
      </div>
      <div v-if="activeSubMenuIndex === index" class="sub-menu show">
        <div v-for="(subItem, subIndex) in menuItem.subMenu" :key="subIndex" class="sub-menu-item">
          {{ subItem }}
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.sidebar {
  background-color: #1E3856;
  color: white;
  width: 250px;
  height: calc(100vh - 20px);
  display: flex;
  flex-direction: column;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  box-shadow: 2px 0px 5px rgba(0, 0, 0, 0.2);
  padding: 20px;
}

.sidebar-header {
  background-color: #0F2340;
  padding: 10px;
  font-size: 17px;
  text-align: center;
  border-bottom: 1px solid #4F7A9C;
  font-weight: 550;
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-bottom: 25px; 
}

.sidebar-header span {
  font-size: 16px;
  margin-bottom: 5px;
}

.sidebar-header .logo-container {
  display: flex;
  align-items: center;
}

.sidebar-header .logo-container {
  display: flex;
  align-items: center;
}

.sidebar-header .logo {
  width: 40px; /* Ajustez la taille du logo selon vos préférences */
  margin-right: 0px; /* Ajustez l'espace entre le logo et le titre selon vos préférences */
}

.menu-item {
  position: relative;
  cursor: pointer;
  margin-bottom: 60px;
  font-size: 19px;
  font-weight: bold;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8);
  margin-left: 12px;
  display: flex;
  align-items: center;
}

.menu-item.long-label {
  flex-direction: column;
  align-items: flex-start;
}

.menu-item .icon {
  margin-right: 8px; /* Ajustez l'espace entre l'icône et le libellé selon vos préférences */
}

.menu-item:hover {
  background-color: #144C73;
}

.sub-menu {
  display: none;
  opacity: 0;
  transition: opacity 0.3s ease;
  margin-top: -10px;
}
.show {
  display: block;
  opacity: 1;
}

.sub-menu.show {
  display: block;
  opacity: 1;
  margin-top: -10px; /* Ajustez la valeur selon vos préférences */
}

.sub-menu-item {
  padding: 10px 10px;
  font-size: 20px;
  border-bottom: 2px solid #4F7A9C;
  transition: background-color 0.3s ease;
}

.sub-menu-item:last-child {
  border-bottom: none;
}

.sub-menu-item:hover {
  background-color: #144C73;
}
</style>

<script>
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faHome, faUser, faSearch, faFile, faCalendar, faMoneyBill, faClock, faPercent,} from '@fortawesome/free-solid-svg-icons';
library.add(faHome, faUser, faSearch, faFile, faCalendar, faMoneyBill, faClock, faPercent,);

export default {
  components: {
    FontAwesomeIcon,
  },
  data() {
    return {
      activeSubMenuIndex: null,
      menuItems: [
        { label: "Accueil", subMenu: ["Sous-tâche 1", "Sous-tâche 2"], icon: ['fas', 'home'] },
        { label: "Patient", subMenu: ["Sous-tâche 1", "Sous-tâche 2"], icon: ['fas', 'user'] },
        { label: "Consultation", subMenu: ["Sous-tâche 1", "Sous-tâche 2"], icon: ['fas', 'search']},
        { label: "Documents", subMenu: ["Sous-tâche 1", "Sous-tâche 2"], icon: ['fas', 'file']},
        { label: "Planning", subMenu: ["Sous-tâche 1", "Sous-tâche 2"], icon: ['fas', 'calendar'] },
        { label: "Facturation", subMenu: ["Sous-tâche 1", "Sous-tâche 2"], icon: ['fas', 'money-bill'] },
        { label: "Honoraire des Gardes", subMenu: ["Sous-tâche 1", "Sous-tâche 2"], icon: ['fas', 'clock'] },
        { label: "Honoraires par taux", subMenu: ["Sous-tâche 1", "Sous-tâche 2"], icon: ['fas', 'percent'] },
        // Ajoutez le reste des éléments de menu ici
      ],
    };
  },
  methods: {
    toggleSubMenu(index) {
      if (this.activeSubMenuIndex === index) {
        this.activeSubMenuIndex = null;
      } else {
        this.activeSubMenuIndex = index;
      }
    },
  },
};
</script> -->

<template>
  <div class="sidebar">
    <div class="sidebar-header">
      <div class="logo-container">
        <img src="../assets/Logo Hannah.jpg" alt="Logo de clinique" class="logo" />
        <span>CLINIQUE HANNAH</span>
      </div>
      <span>MENU</span>
    </div>
    <div v-for="(menuItem, index) in menuItems" :key="index">
      <div :class="{'menu-item': true, 'with-submenu': menuItem.hasSubMenu }" @click="toggleSubMenu(index)">
        <FontAwesomeIcon :icon="menuItem.icon" class="icon" />
        {{ menuItem.label }}
      </div>
      <!-- <transition name="fade"> -->
        <div v-if="activeSubMenuIndex === index" class="sub-menu">
          <div v-for="(subItem, subIndex) in menuItem.subMenu" :key="subIndex" class="sub-menu-item">
            {{ subItem }}
          </div>
        </div>
      <!-- </transition> -->
    </div>
  </div>
</template>

<style scoped>
.sidebar {
  background-color: #1E3856;
  color: white;
  width: 250px;
  height: calc(100vh - 20px);
  display: flex;
  flex-direction: column;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  box-shadow: 2px 0px 5px rgba(0, 0, 0, 0.2);
  padding: 20px;
}

.sidebar-header {
  background-color: #0F2340;
  padding: 10px;
  font-size: 17px;
  text-align: center;
  border-bottom: 1px solid #4F7A9C;
  font-weight: 550;
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-bottom: 25px; 
}

.sidebar-header span {
  font-size: 16px;
  margin-bottom: 5px;
}

.sidebar-header .logo-container {
  display: flex;
  align-items: center;
}

.sidebar-header .logo {
  width: 40px; /* Ajustez la taille du logo selon vos préférences */
  margin-right: 0px; /* Ajustez l'espace entre le logo et le titre selon vos préférences */
}

.menu-item {
  position: relative;
  cursor: pointer;
  margin-bottom: 50px;
  font-size: 19px;
  font-weight: bold;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8);
  margin-left: 12px;
  display: flex;
  align-items: center;
}

.with-submenu {
  margin-bottom: 50px; /* Ajustez la valeur selon vos préférences */
}

.menu-item.long-label {
  flex-direction: column;
  align-items: flex-start;
}

.menu-item .icon {
  margin-right: 8px; /* Ajustez l'espace entre l'icône et le libellé selon vos préférences */
}

.menu-item:hover {
  background-color: #144C73;
}

.sub-menu {
  display: block;
  opacity: 1;
  transition: opacity 0.3s ease;
  margin-top: -10px; /* Ajustez la valeur selon vos préférences */
}

.sub-menu-item {
  padding: 10px 10px;
  font-size: 20px;
  border-bottom: 2px solid #4F7A9C;
  transition: background-color 0.3s ease;
}

.sub-menu-item:last-child {
  border-bottom: none;
}

.sub-menu-item:hover {
  background-color: #144C73;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>

<script>
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faHome, faUser, faSearch, faFile, faCalendar, faMoneyBill, faClock, faPercent, faCogs} from '@fortawesome/free-solid-svg-icons';
library.add(faHome, faUser, faSearch, faFile, faCalendar, faMoneyBill, faClock, faPercent, faCogs);

export default {
  components: {
    FontAwesomeIcon,
  },
  data() {
    return {
      activeSubMenuIndex: null,
      menuItems: [
        { label: "Accueil", subMenu: ["Sous-tâche 1", "Sous-tâche 2"], icon: ['fas', 'home'], hasSubMenu: true },
        { label: "Patient", subMenu: ["Gestion des Patients", "Patients en Attentes"], icon: ['fas', 'user'], hasSubMenu: true },
        { label: "Consultation", subMenu: ["Gestion des Medecins", "Gestion des Rendez-Vous"], icon: ['fas', 'search'], hasSubMenu: true },
        { label: "Documents", subMenu: ["Sous-tâche 1", "Sous-tâche 2"], icon: ['fas', 'file'], hasSubMenu: true },
        { label: "Planning", subMenu: ["Sous-tâche 1", "Sous-tâche 2"], icon: ['fas', 'calendar'], hasSubMenu: true },
        { label: "Facturation", subMenu: ["Factures aux assureurs", "Factures en attentes"], icon: ['fas', 'money-bill'], hasSubMenu: true },
        { label: "Honoraire des Gardes", subMenu: ["Integration du calendrier", "Calcul honoraires des gardes"], icon: ['fas', 'clock'], hasSubMenu: true },
        { label: "Honoraires par taux", subMenu: ["Sous-tâche 1", "Sous-tâche 2"], icon: ['fas', 'percent'], hasSubMenu: true },
        { label: "Paramètres", subMenu: ["Sous-tâche 1", "Sous-tâche 2"], icon: ['fas', 'cogs'] },
        // Ajoutez le reste des éléments de menu ici
      ],
    };
  },
  methods: {
    toggleSubMenu(index) {
      this.activeSubMenuIndex = (this.activeSubMenuIndex === index) ? null : index;
    },
  },
};
</script>
